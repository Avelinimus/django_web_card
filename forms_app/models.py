from django.db import models


class Support(models.Model):
    class Meta:
        ordering = ['name']
        verbose_name = 'Сообщения поддержки'
        verbose_name_plural = 'Сообщение поддержки'

    name = models.CharField(max_length=100, verbose_name='Имя', db_index=True)
    email = models.EmailField(max_length=100, verbose_name='E-mail', db_index=True)
    comment = models.TextField(verbose_name='Комментарий', db_index=True)

    def __str__(self):
        return self.name