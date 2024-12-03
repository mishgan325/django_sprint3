from django.db import models

from django.contrib.auth import get_user_model

User = get_user_model()


class AbstractModel(models.Model):
    is_published = models.BooleanField(
        'Опубликовано',
        default=True,
        help_text='Снимите галочку, чтобы скрыть публикацию.'
    )
    created_at = models.DateTimeField('Добавлено',
                                      auto_now_add=True
                                      )

    class Meta:
        abstract = True


class Category(AbstractModel):
    title = models.CharField('Заголовок',
                             max_length=256
                             )
    description = models.TextField('Описание')
    slug = models.SlugField(
        'Идентификатор',
        unique=True,
        help_text=(
            'Идентификатор страницы для URL; разрешены символы латиницы, '
            + 'цифры, дефис и подчёркивание.'
        )
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'Категории'


class Location(AbstractModel):
    name = models.CharField(
        'Название места',
        max_length=256
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'местоположение'
        verbose_name_plural = 'Местоположения'


class Post(AbstractModel):
    title = models.CharField('Заголовок', max_length=256)
    text = models.TextField('Текст')
    pub_date = models.DateTimeField(
        'Дата и время публикации',
        auto_now=False,
        auto_now_add=False,
        help_text='Если установить дату и время в будущем'
        + ' — можно делать отложенные публикации.'
    )
    author = models.ForeignKey(User,
                               verbose_name='Автор публикации',
                               on_delete=models.CASCADE
                               )
    location = models.ForeignKey(Location,
                                 verbose_name='Местоположение',
                                 null=True,
                                 on_delete=models.SET_NULL
                                 )
    category = models.ForeignKey(Category,
                                 verbose_name='Категория',
                                 null=True,
                                 on_delete=models.SET_NULL
                                 )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'публикация'
        verbose_name_plural = 'Публикации'
        ordering = ['-pub_date']
