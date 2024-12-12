from celery import Celery
from django.core.mail import send_mail


app = Celery('LaMarqueza', broker='redis://localhost:6379/0')

@app.task
def enviar_correo(asunto, mensaje, remitente, destinatarios):
    send_mail(asunto, mensaje, remitente, destinatarios)