# auth.py
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
import os
import pickle
from requests import Request
from dotenv import load_dotenv

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

# Escopo de permissão (permite ler e-mails)
SCOPES = os.getenv("GMAIL_API_SCOPES").split(',')

def authenticate_gmail():
    """Autentica o usuário e retorna o serviço da API Gmail."""
    creds = None

    # O arquivo token.pickle armazena o token de acesso do usuário.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)

    # Se não tiver credenciais válidas, solicita ao usuário para fazer login
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)

        # Salvar as credenciais para a próxima vez
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    return creds
