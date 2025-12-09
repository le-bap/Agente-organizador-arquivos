import os
from agent import decide_action, executar_acao

PASTA_MONITORADA = r"C:\Users\Letizia\Documents\teste"
DESTINO = r"C:\Users\Letizia\Documents\teste\Organizado"

def main():
    arquivos = os.listdir(PASTA_MONITORADA)

    if not arquivos:
        print("Nenhum arquivo para organizar.")
        return

    for arquivo in arquivos:
        caminho = os.path.join(PASTA_MONITORADA, arquivo)

        if os.path.isdir(caminho):
            continue

        categoria = decide_action(arquivo)
        executar_acao(caminho, DESTINO, categoria)

        print(f"{arquivo} → {categoria}")

if __name__ == "__main__":
    main()
