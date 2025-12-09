import os
import shutil
import json
import subprocess

MODEL = "phi3"

# tenta classificar antes nas extensões mais conhecidas
CATEGORIAS = {
    ".jpg": "Imagens",
    ".jpeg": "Imagens",
    ".png": "Imagens",
    ".gif": "Imagens",

    ".pdf": "PDFs",
    ".docx": "Documentos",
    ".txt": "Textos",

    ".py": "Codigo",
    ".js": "Codigo",
    ".java": "Codigo",

    ".mp4": "Videos",
    ".mkv": "Videos",
    ".mov": "Videos",

    ".zip": "Compactados",
    ".rar": "Compactados"
}

def run_model(prompt: str) -> str:
    # Executa o modelo local via Ollama.
    process = subprocess.Popen(
        ["ollama", "run", MODEL],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        encoding="utf-8",
        errors="replace"
    )
    output, _ = process.communicate(prompt)
    return output

def decide_action_ia(filename: str) -> str:
    
    prompt = f"""
    Você é um agente que organiza arquivos automaticamente.
    Para o arquivo abaixo, retorne APENAS um JSON no formato:
    {{
    "acao": "mover",
    "destino": "Imagens"
    }}

    Arquivo: {filename}

    Organize pela extensão: pdf, jpg, png, txt, mp4, zip, py, etc.
    Se não souber, coloque destino como "Outros".
    """

    response = run_model(prompt) # roda o prompt no modelo

    try:
        json_start = response.find("{")
        json_end = response.rfind("}") + 1
        data = json.loads(response[json_start:json_end])
        return data
    except:
        return {"acao": "mover", "destino": "Outros"}

def decide_action(filename: str) -> str:
    ext = os.path.splitext(filename)[1].lower()
    print(ext)

    # 1) Se a extensão for conhecida ja encaminha pra pasta certa
    if ext in CATEGORIAS:
        return CATEGORIAS[ext]

    # 2) Extensão desconhecida usa IA
    data = decide_action_ia(filename)
    return data["destino"]


def executar_acao(filepath: str, destino_base: str, destino: str):
    # Move o arquivo para a pasta de destino.
    destino_path = os.path.join(destino_base, destino)

    os.makedirs(destino_path, exist_ok=True)
    shutil.move(filepath, destino_path)
