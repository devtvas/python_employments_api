# gmail_api.py
from auth import authenticate_gmail
from googleapiclient.discovery import build

def get_gmail_service():
    """Retorna o serviço da API Gmail autenticado."""
    creds = authenticate_gmail()
    service = build('gmail', 'v1', credentials=creds)
    return service
