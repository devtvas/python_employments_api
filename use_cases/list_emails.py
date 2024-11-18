# use_cases/list_emails.py
from gmail_api import get_gmail_service

def list_emails():
    """Caso de uso para listar os e-mails não lidos da caixa de entrada."""
    service = get_gmail_service()

    # Chamar a API Gmail para listar os e-mails
    results = service.users().messages().list(userId='me', labelIds=['INBOX'], q="is:unread").execute()
    messages = results.get('messages', [])

    if not messages:
        print("Nenhum e-mail encontrado.")
    else:
        print("E-mails encontrados:")
        for message in messages[:5]:  # Limite de 5 e-mails para exibir
            msg = service.users().messages().get(userId='me', id=message['id']).execute()
            print(f"Assunto: {msg['snippet']}")
