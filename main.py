import os
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import google.generativeai as genai
from dotenv import load_dotenv

# ===== CARREGAR VARIÁVEIS DE AMBIENTE =====
load_dotenv()

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not TELEGRAM_TOKEN or not GEMINI_API_KEY:
    raise ValueError("⚠️ Erro: TELEGRAM_TOKEN ou GEMINI_API_KEY não configurados no .env")

genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

# ===== COMANDOS =====
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Comando /start - Mensagem de boas-vindas"""
    await update.message.reply_text(
        "🤖 Olá! Sou seu bot com Gemini.\n\n"
        "Me mande qualquer pergunta que eu respondo com IA!\n"
        "Ex: 'Me explique o que é Python'\n\n"
        "Estou pronto para ajudar! 🚀"
    )

async def conversar(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handler para mensagens de texto - Processa e responde com Gemini"""
    user_text = update.message.text
    
    # Mensagem de loading
    loading_msg = await update.message.reply_text("🧠 Pensando...")
    
    try:
        # Gera resposta usando Gemini
        resposta = model.generate_content(user_text)
        texto = resposta.text
        
        # Deleta mensagem de loading
        await loading_msg.delete()
        
        # Envia resposta em partes se for muito longa
        if len(texto) > 4000:
            for i in range(0, len(texto), 4000):
                await update.message.reply_text(texto[i:i+4000])
        else:
            await update.message.reply_text(texto)
            
    except Exception as e:
        await loading_msg.delete()
        await update.message.reply_text(f"❌ Erro ao processar: {str(e)}")

async def erro_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handler para erros"""
    print(f"❌ Erro: {context.error}")

# ===== MAIN =====
if __name__ == '__main__':
    print("🚀 Iniciando Bot Drive...")
    
    app = Application.builder().token(TELEGRAM_TOKEN).build()
    
    # Adiciona handlers
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, conversar))
    app.add_error_handler(erro_handler)
    
    print("✅ Bot rodando... Pressione Ctrl+C para parar")
    app.run_polling()
