import smtplib
from email.message import EmailMessage
from celery import Celery

from config import SMTP_USER, SMTP_PASS


SMTP_HOST = 'smtp.gmail.com'
SMTP_PORT = 465


celery = Celery('tasks',broker='redis://localhost')


def get_email_template_dashboard(username:str):
    email = EmailMessage()
    email['Subject'] = 'billing...'
    email['From'] = SMTP_USER
    email['To'] = SMTP_USER
    email.set_content(
        f'<div>{username} a plotit budem?</div>', subtype = 'html'
    )
    return email
    
    

@celery.task
def send_email_report_dashboard(username):
    email = get_email_template_dashboard(username)
    with smtplib.SMTP_SSL(SMTP_HOST,SMTP_PORT) as server:
        server.login(SMTP_USER,SMTP_PASS)
        server.send_message(email)