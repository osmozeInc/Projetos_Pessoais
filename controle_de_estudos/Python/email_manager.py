import re
import smtplib

email_padrao = r'^[\w\.-]+@[\w\.-]+\.\w+$'

def validar_email(email_client):
    if re.match(email_padrao, email_client):
        return True
    else:
        return False


class Email_de_Recuperacao():
    def __init__(self, email_client, email_padrao):
        self.email_client = email_client

    def Enviar_Email_Recuperacao(self):
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login('caioxgmm0444@gmail.com', 'xxxxxxx!')
        server.sendmail('caioxgmm0444@gmail.com', 'ssobral@yahoo.com.br', 'Recuperação de senha')
        server.quit()