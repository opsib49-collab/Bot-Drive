import os
import google.generativeai as genai
from drive_search import buscar_arquivos, ler_conteudo_arquivo
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel('gemini-1.5-flash')

def ler_conteudo_arquivo(file_id):
    """Lê conteúdo de arquivos texto/Google Docs"""
    from googleapiclient.discovery import build
    from google.oauth2.credentials import Credentials
    import pickle
    
    with open('token.pickle', 'rb') as token:
        creds = pickle.load(token)
    
    service = build('drive', 'v3', credentials=creds)
    
    try:
        doc = service.files().export_media(
            fileId=file_id,
            mimeType='text/plain'
        ).execute()
        return doc.decode('utf-8')
    except:
        return None

def responder_com_drive(pergunta):
    """Pesquisa no Drive e usa Gemini para responder"""
    
    arquivos = buscar_arquivos(pergunta)
    
    if not arquivos:
        return "❌ Nenhum arquivo encontrado no Drive sobre esse assunto."
    
    contextos = []
    for arquivo in arquivos[:3]:
        try:
            conteudo = ler_conteudo_arquivo(arquivo['id'])
            if conteudo:
                contextos.append(f"Arquivo: {arquivo['name']}\nConteúdo: {conteudo[:2000]}")
            else:
                contextos.append(f"Arquivo: {arquivo['name']}\nLink: {arquivo['webViewLink']}")
        except:
            contextos.append(f"Arquivo: {arquivo['name']}\nLink: {arquivo['webViewLink']}")
    
    prompt = f"""
    Baseado nos seguintes documentos do Google Drive, responda a pergunta do usuário.
    
    Documentos encontrados:
    {'---'.join(contextos)}
    
    Pergunta do usuário: {pergunta}
    
    Responda de forma clara, citando quais arquivos foram usados.
    """
    
    resposta = model.generate_content(prompt)
    return resposta.text
