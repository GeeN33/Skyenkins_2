from celery import shared_task
from Skyenkins_2.celery import app
from django.conf import settings
from django.core.mail import send_mail
import subprocess
from users.models import User
from appfiles.models import Files
import os


@app.task
def checked_files():
    MEDIA_ROOT = settings.MEDIA_ROOT

    str_rez = '\n+++++++++++++++++++++++++\n'
    users = User.objects.all()
    for user in users:
        files = Files.objects.filter(author=user)
        str_rez += '================== \n'
        str_rez += 'user email = ' + user.email + '\n'
        for file in files:
            f = MEDIA_ROOT + '/' + file.file.__str__()
            str_rez += '---------------\n'
            file_name = f

            str_rez += 'file name = ' + file_name + '\n'
            # log = subprocess.run(["flake8", f], stdout=subprocess.PIPE, text=True)
            # str_rez += log.stdout + '/n'
            # log = subprocess.call(["flake8",'--config','.flake8.ini', file.file])
            # str_rez += log + '/n'
        #
        # print(str_rez)
    return str_rez






def send_email():
    try:
        print('my send_email')
        send_mail('Ура ты крут', 'Тело письма', settings.EMAIL_HOST_USER, ['evgeniy.1@mail.ru'])
        return 'Ура ты крут'

    except:

        return 'Ну ты не крут'


