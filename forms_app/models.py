from django.db import models


class Order(models.Model):
    class Meta:
        ordering = ['email']
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    name = models.CharField(max_length=100, verbose_name='Имя', db_index=True)
    surname = models.CharField(max_length=100, verbose_name='Фамилия', db_index=True, blank=True)
    telephone = models.CharField(max_length=12, verbose_name='Мобильный телефон', default='380', blank=True)
    email = models.EmailField(verbose_name='E-mail', db_index=True)
    time = models.CharField(max_length=30, verbose_name='Удобное время', default='Не важно', blank=True)
    comment = models.CharField(max_length=200, verbose_name='Комментарий', blank=True)


class Support(models.Model):
    class Meta:
        ordering = ['email']
        verbose_name = 'Сообщение поддержки'
        verbose_name_plural = 'Сообщения поддержки'

    name = models.CharField(max_length=100, verbose_name='Имя', db_index=True)
    email = models.EmailField(max_length=100, verbose_name='E-mail', db_index=True)
    comment = models.TextField(verbose_name='Комментарий', db_index=True)

    def __str__(self):
        return self.email
