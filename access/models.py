from django.db import models


# Класс модели пользователей сайта
class User(models.Model):

    login = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    reg_date = models.DateTimeField()
    status = models.CharField(max_length=50)

