from celery import shared_task
from Skyenkins_2.celery import app

@app.task
def send_email():
    print('send_email')