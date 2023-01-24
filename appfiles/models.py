from django.db import models
from users.models import User


class Files(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь', blank=False, null=True)
    file = models.FileField(upload_to='file/')
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    checked_text = models.TextField(null=True, blank=True)
    checked = models.BooleanField(default=False, null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Файл"
        verbose_name_plural = "Файлы"

class Logs(models.Model):

    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь', blank=False, null=True)
    files = models.ForeignKey(Files, on_delete=models.CASCADE, verbose_name='Файлы', blank=False, null=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    log_text = models.TextField(null=True, blank=True)

    def __str__(self):
        return "log"

    class Meta:
        verbose_name = "log"
        verbose_name_plural = "logs"