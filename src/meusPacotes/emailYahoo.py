import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# https://br.ajuda.yahoo.com/kb/Gerar-e-gerenciar-senhas-de-aplicativos-de-terceiros-sln15241.html

def enviar_email(usuario, senha, destinatario, assunto, mensagem):
    # Configurações do servidor SMTP do Yahoo
    servidor_smtp = 'smtp.mail.yahoo.com'
    porta = 587
    # Criar objeto do tipo MIMEMultipart
    msg = MIMEMultipart()
    msg['From'] = usuario
    msg['To'] = destinatario
    msg['Subject'] = assunto
    # Adicionar mensagem ao corpo do e-mail
    msg.attach(MIMEText(mensagem, 'plain'))
    # Iniciar conexão com o servidor SMTP do Yahoo
    servidor = smtplib.SMTP(servidor_smtp, porta)
    servidor.starttls()
    # Autenticar no servidor SMTP
    servidor.login(usuario, senha)
    # Enviar e-mail
    servidor.sendmail(usuario, destinatario, msg.as_string())
    # Fechar conexão com o servidor SMTP
    servidor.quit()