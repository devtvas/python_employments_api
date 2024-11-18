
# Projeto de Leitura de E-mails e Armazenamento em Banco de Dados

Este projeto é um software em Python para acessar e-mails (como o Outlook), buscar e-mails de um dia específico por palavras-chave (ex.: "candidatura foi enviada"), armazenar esses e-mails em um banco de dados relacional (PostgreSQL) e disponibilizar os dados via API.

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

## Requisitos

Antes de começar, certifique-se de ter o Python instalado no seu sistema.

- Python 3.x
- PostgreSQL (para armazenar os e-mails)
- Acesso à conta de e-mail (ex.: Outlook)

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

## Como Programar

### 1. Acessar e-mails

No arquivo `email_reader.py`, o código conecta-se ao servidor IMAP do Outlook (ou de outro provedor de e-mail) e busca e-mails com base em palavras-chave e data.

Para rodar o código de exemplo:

1. **Edite o arquivo `email_reader.py` com suas credenciais de e-mail (username e password)**.
2. **Execute o código:**

   ```bash
   python email_reader.py
    ```

3. **Isso conectará ao servidor de e-mail e exibirá os e-mails que atendem aos critérios de pesquisa (palavra-chave e data).**

## Executando o Projeto
Para rodar o código e testar a conexão com o servidor IMAP, execute o arquivo **main.py:**

   ```bash
   $ python main.py
  ```
    
## Próximos Passos
Agora que você já pode acessar e-mails, o próximo passo é processá-los e armazená-los em um banco de dados. Vamos configurar o PostgreSQL e criar a API que irá disponibilizar os e-mails.

## Dependências do Projeto
Este projeto utiliza as seguintes dependências:

- imaplib - Para acessar e-mails via IMAP.
- email - Para fazer parsing e extrair os dados dos e-mails.
- requests - Para interagir com APIs (caso necessário).


## Licença
Este projeto é de uso pessoal e educacional. Para usos comerciais, entre em contato para discutir a licença.