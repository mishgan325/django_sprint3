from django.db import models

from django.contrib.auth import get_user_model

User = get_user_model()


class Category(models.Model):
    title = models.CharField('Заголовок',
                             max_length=256
                             )
    description = models.TextField('Описание')
    slug = models.SlugField('Идентификатор',
                            help_text='Идентификатор страницы для URL; разрешены символы латиницы, цифры, дефис и подчёркивание.'
                            )
    is_published = models.BooleanField('Опубликовано',
                                       default=True,
                                       help_text='Снимите галочку, чтобы скрыть публикацию.'
                                       )
    created_at = models.DateTimeField('Добавлено',
                                      auto_now_add=True
                                      )

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'Категории'


class Location(models.Model):
    name = models.CharField('Название места',
                             max_length=256
                             )
    is_published = models.BooleanField('Опубликовано',
                                       default=True
                                       )
    created_at = models.DateTimeField('Добавлено',
                                      auto_now_add=True
                                      )

    class Meta:
        verbose_name = 'местоположение'
        verbose_name_plural = 'Местоположения'


class Post(models.Model):
    title = models.CharField('Имя', max_length=256)
    text = models.TextField('Текст')
    pub_date = models.DateField("Дата и время публикации",
                                 auto_now=False,
                                 auto_now_add=False,
                                 help_text='Если установить дату и время в будущем — можно делать отложенные публикации.'
                                 )
    author = models.ForeignKey(User,
                               verbose_name='Автор публикации',
                               on_delete=models.CASCADE
                               )
    location = models.ForeignKey(Location,
                                 verbose_name='Местоположение',
                                 on_delete=models.CASCADE
                                 )
    category = models.ForeignKey(Category,
                                 verbose_name='Категория',
                                 on_delete=models.CASCADE
                                 )
    is_published = models.BooleanField('Опубликовано',
                                       default=True
                                       )
    created_at = models.DateTimeField('Добавлено',
                                      auto_now_add=True
                                      )

    class Meta:
        verbose_name = 'публикация'
        verbose_name_plural = 'Публикации'
