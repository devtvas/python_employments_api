
# Projeto de Leitura de E-mails e Armazenamento em Banco de Dados

Este projeto é um software em Python para acessar e-mails (como o Outlook), buscar e-mails de um dia específico por palavras-chave (ex.: "candidatura foi enviada"), armazenar esses e-mails em um banco de dados relacional (PostgreSQL) e disponibilizar os dados via API.

## Requisitos

Antes de começar, certifique-se de ter o Python instalado no seu sistema.

- Python 3.x
- PostgreSQL (para armazenar os e-mails)
- Acesso à conta de e-mail (ex.: Outlook ou Gmail)

## Configuração Inicial

1. **Clone este repositório**:
    ```bash
    git clone https://seu-repositorio.git
    cd employments_api
    ```

2. **Crie um ambiente virtual**:
    - No terminal, dentro da pasta do projeto, crie o ambiente virtual:
      ```bash
      python -m venv venv
      ```
      
3. **Ative o ambiente virtual**:
    - No Windows:
      ```bash
      venv\Scripts\activate
      ```
    - No macOS/Linux:
      ```bash
      source venv/bin/activate
      ```

4. **Instale as dependências**:
    - Para instalar as dependências necessárias, execute:
      ```bash
      pip install -r requirements.txt
      ```
      
5. **Verifique a lista de Imap**
  - https://www.systoolsgroup.com/imap/

6. **Crie uma senha de Aplicativo**
https://myaccount.google.com/apppasswords?hl=pt_BR&rapt=AEjHL4PGiNaCWHc5d0EMDH-1j-cDXcvYu0LSuGEIB1dUzT43oM_98QVyaIdkWKeEfQELMLE56myo9AODDKUCxH_SyZQiEJO0PtiogkzeDuQe5UNXFQsU3eU

7. **Configuração do PostgreSQL**:
    - Crie um banco de dados no PostgreSQL para armazenar os e-mails.
    - Configure a conexão com o banco de dados no arquivo `database.py`.



## Executando o Projeto
Para rodar o código e testar a conexão com o servidor de email, execute o arquivo **main.py:**

   ```bash
   $ python main.py
  ```

## Importante - Atualizar o Token diariamente!

1. **Remover o arquivo `token.pickle`**:
   A maneira mais simples de atualizar o **token de acesso** é excluir o arquivo **`token.pickle`** que contém os tokens de acesso e atualização armazenados do dia anterior.

   Para remover o arquivo `token.pickle`, execute o seguinte comando:

   ```bash
   rm token.pickle
    ```
    
## Próximos Passos
Agora que você já pode acessar e-mails, o próximo passo é processá-los e armazená-los em um banco de dados. Vamos configurar o PostgreSQL e criar a API que irá disponibilizar os e-mails.

## Estrutura do Projeto

A estrutura inicial do projeto é a seguinte:

```
employments_api/
    ├── venv/               
    ├── main.py              
    ├── auth.py             
    ├── gmail_api.py        
    ├── use_cases/          
    │   └── list_emails.py
    ├── .env                
    ├── requirements.txt
    └── README.md     
```

## Dependências do Projeto
Este projeto utiliza as seguintes dependências:

- imaplib - Para acessar e-mails via IMAP.
- email - Para fazer parsing e extrair os dados dos e-mails.
- requests - Para interagir com APIs (caso necessário).

## Licença
Este projeto é de uso pessoal e educacional. Para usos comerciais, entre em contato para discutir a licença.