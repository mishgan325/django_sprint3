from django.db import models

from django.contrib.auth import get_user_model

User = get_user_model()


class Category(models.Model):
    title = models.CharField('Имя', max_length=256)
    description = models.TextField('Описание')
    slug = models.SlugField('Slug')
    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)


class Location(models.Model):
    name = models.CharField('Название', max_length=256)
    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)


class Post(models.Model):
    title = models.CharField('Имя', max_length=256)
    text = models.TextField('Текст')
    pub_date = models.DateField("Дата публикации", auto_now=False, auto_now_add=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
