from celery import shared_task
from Skyenkins_2.celery import app
from django.conf import settings
from django.core.mail import send_mail
import subprocess
from users.models import User
from appfiles.models import Files, Logs
import os

def send_email(text):
    try:

        send_mail('log', text, settings.EMAIL_HOST_USER, ['evgeniy.1@mail.ru'])
        return 'Ура ты крут'

    except:

        return 'Ну ты не крут'


@app.task
def checked_files():
    str_rez = '\n+++++++++++++++++++++++++\n'
    users = User.objects.all()
    for user in users:
        files = Files.objects.filter(author=user)
        str_rez += '================== \n'
        str_rez += 'user email = ' + user.email + '\n'

        for file in files:
            file.checked = True
            str_rez += '---------------\n'
            file_name = file.file.path
            str_rez += 'file name = ' + file_name + '\n'
            file.save()
            log = subprocess.run(["flake8", file.file.path], stdout=subprocess.PIPE, text=True)
            str_rez += log.stdout + '/n'
            # log = subprocess.call(["flake8",'--config','.flake8.ini', file.file])
            # str_rez += log + '/n'
            file.checked_text = str_rez
            file.save()
            Logs.objects.create(
            author=user,
            files = file,
            log_text = str_rez)

        #
        print(str_rez)
        send_email(str_rez)

    return str_rez


