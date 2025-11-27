import imaplib
from dotenv import load_dotenv # type: ignore
import os

load_dotenv()

email = os.getenv("EMAIL")
senha = os.getenv("SENHA_API")
servidor_imap = 'imap.gmail.com'

def conectar_email():
    mail = imaplib.IMAP4_SSL(servidor_imap)
    status , response = mail.login(email,senha)
    mail.select("inbox")
    
    if status == "OK":
            print("Conectado e logado com sucesso!")
    else:
            print("Erro ao fazer login:", response)
