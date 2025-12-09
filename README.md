# Agente-organizador-arquivos 🗂️

Um agente simples em Python que organiza automaticamente os arquivos de uma pasta, movendo-os para categorias apropriadas (imagens, PDFs, compactados, etc). Usa classificação por extensão para a maioria dos arquivos e recorre a um modelo local de linguagem (phi3 + Ollama) somente para extensões desconhecidas. Desta forma, ele combina **velocidade e confiabilidade** com **inteligência** quando necessário.

---

## ✅ Funcionalidades

- Classificação automática por extensão (jpg, png, pdf, py, mp4, zip etc) — sem IA, instantâneo  
- Fallback com IA (phi3) para casos de extensões desconhecidas 
- Criação automática de pastas de destino se não existirem  
- Organização de arquivos movendo de uma pasta-origem para pasta-destino  
- Código simples, direto e fácil de entender  

---

## 🛠️ Tecnologias & dependências

- Python 3  
- Bibliotecas padrão do Python: `os`, `shutil`, `json`, `subprocess`  
- Ollama + modelo local **phi3**  
- Sistema operacional compatível com Ollama (Windows / Linux / macOS), se usar fallback IA  

---

## 📥 Como usar

1. Clone este repositório:  
   ```bash
   git clone https://github.com/le-bap/Agente-organizador-arquivos.git
   cd Agente-organizador-arquivos
2. se quiser usar o fallback com IA: instale e configure o Ollama + modelo phi3
3. Abra main.py. Altere as variáveis conforme sua pasta de origem e destino

   Exemplo no Windows:
   ```bash
   PASTA_MONITORADA = r"C:\Users\SeuUsuario\Downloads"
   DESTINO = r"C:\Users\SeuUsuario\Documents\Organizado"

5. Execute:
   ```bash
   python3 main.py
   
