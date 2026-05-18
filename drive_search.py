import os
import pickle
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

SCOPES = ['https://www.googleapis.com/auth/drive.readonly']

def autenticar_drive():
    """Autentica e retorna serviço do Google Drive"""
    creds = None
    
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)
    
    return build('drive', 'v3', credentials=creds)

def buscar_arquivos(consulta, max_resultados=10):
    """Busca arquivos no Google Drive"""
    service = autenticar_drive()
    
    query = f"name contains '{consulta}' or fullText contains '{consulta}'"
    
    results = service.files().list(
        q=query,
        fields="files(id, name, webViewLink, mimeType, modifiedTime)",
        pageSize=max_resultados
    ).execute()
    
    return results.get('files', [])
