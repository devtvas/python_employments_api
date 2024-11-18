
def display_emails(emails):
    """Função para exibir os e-mails de forma amigável na tela."""
    if not emails:
        print("Nenhum e-mail para exibir.")
        return

    print("E-mails encontrados:")
    for email in emails:
        print(f"Assunto: {email['subject']}")
        print(f"De: {email['from']}")
        print("-" * 40)
