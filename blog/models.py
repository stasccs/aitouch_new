from django.db import models
from tinymce import models as tinymce_model


# Класс модели публикации новости
class Post1(models.Model):

    title = models.CharField(max_length=100)
    annotation = models.CharField(max_length=256)
    content = models.TextField()
    link = models.CharField(max_length=100)
    photo = models.CharField(max_length=100)
    publish = models.DateTimeField()
    status = models.CharField(max_length=50)


class Blog(models.Model):

    title = models.CharField(max_length=150)
    annotation = models.CharField(max_length=400)
    content = models.TextField()
    photo = models.ImageField(upload_to='media')
    publish = models.DateTimeField()


class Blog1(models.Model):

    title = models.CharField(max_length=150)
    annotation = models.CharField(max_length=400)
    content = models.TextField()
    photo = models.ImageField()
    publish = models.DateTimeField()