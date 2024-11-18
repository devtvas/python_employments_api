# main.py
from use_cases.list_emails import list_emails
from display.display_emails import display_emails

def main():
    emails = list_emails(query="is:unread", max_results=5)
    display_emails(emails)

if __name__ == '__main__':
    main()
