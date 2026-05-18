import os
from dotenv import load_dotenv
from gemini_ia import responder_com_drive

load_dotenv()

def main():
    print("🤖 Assistente do Google Drive (digite 'sair' para encerrar)")
    print("=" * 50)
    
    while True:
        pergunta = input("\n📝 Sua pergunta: ").strip()
        
        if pergunta.lower() in ['sair', 'exit', 'quit']:
            print("👋 Até logo!")
            break
        
        if not pergunta:
            continue
        
        print("\n🔍 Pesquisando no Google Drive e processando com IA...")
        resposta = responder_com_drive(pergunta)
        print(f"\n🤖 Resposta:\n{resposta}")

if __name__ == "__main__":
    main()
