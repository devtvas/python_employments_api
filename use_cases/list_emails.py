# use_cases/list_emails.py
from gmail_api import get_gmail_service

def list_emails(query="is:unread", max_results=5, label="INBOX"):
    """Caso de uso para listar os e-mails com base em critérios específicos."""
    service = get_gmail_service()

    try:
        # Chamar a API Gmail para listar os e-mails com base no filtro
        results = service.users().messages().list(
            userId='me',
            labelIds=[label],
            q=query,
            maxResults=max_results  # Limitar o número de resultados
        ).execute()

        messages = results.get('messages', [])
        
        if not messages:
            print("Nenhum e-mail encontrado.")
            return []

        emails = []

        # Para cada e-mail encontrado, obtenha mais detalhes
        for message in messages:
            msg = service.users().messages().get(userId='me', id=message['id']).execute()
            email_data = {
                'subject': msg['snippet'],  # Aqui podemos melhorar para pegar o assunto real
                'id': msg['id'],
                'from': msg['payload']['headers'][0]['value']  # Exemplo de pegar o 'De'
            }
            emails.append(email_data)

        return emails

    except Exception as e:
        print(f"Erro ao tentar listar e-mails: {e}")
        return []
