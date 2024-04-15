from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=250, verbose_name='Заголовок')
    body = models.TextField(blank=True, null=True, verbose_name='Содержимое')
    preview = models.ImageField(upload_to='blogs/images', blank=True, null=True, verbose_name='Изображение')
    date_is_published = models.DateField(blank=True, null=True, verbose_name='Дата публикации')
    views_count = models.IntegerField(default=0, verbose_name='Просмотры')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Блог'
        verbose_name_plural = 'Блоги'
