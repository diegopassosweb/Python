#Primeiro ative os 2 fatores na sua conta

from email.message import EmailMessage
from app2 import password
import ssl
import smtplib

email_sender = 'fulano@gmail.com'
email_password = password

email_receiver = 'email temporario aqui'

subject = 'Dont forget to subscribe'
body = """
Watch a video
"""

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendemail(email_sender, email_receiver, em.as_string())