from django.db import models


class Order(models.Model):
    class Meta:
        ordering = ['email']
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    name = models.CharField(max_length=100, verbose_name='Имя', db_index=True)
    surname = models.CharField(max_length=100, verbose_name='Фамилия', db_index=True, blank=True)
    telephone = models.CharField(max_length=12, verbose_name='Мобильный телефон', default='380', blank=True)
    email = models.EmailField(verbose_name='E-mail', db_index=True, max_length=30)
    time = models.CharField(max_length=30, verbose_name='Удобное для вас время', default='Не важно', blank=True)
    service = models.CharField(max_length=20, choices=(('Визитка', 'Визитка'),
                                                      ('Интернет-магазин', 'Интернет-магазин'),
                                                      ('Уникальный сайт', 'Уникальный сайт')),
                               default='Уникальный сайт', verbose_name='Услуга')
    comment = models.CharField(max_length=200, verbose_name='Комментарий', blank=True)
    flag = models.BooleanField(blank=True, verbose_name='Оповестить Вас на почте?', default=False)


class Support(models.Model):
    class Meta:
        ordering = ['email']
        verbose_name = 'Сообщение поддержки'
        verbose_name_plural = 'Сообщения поддержки'

    name = models.CharField(max_length=100, verbose_name='Имя', db_index=True)
    email = models.EmailField(max_length=100, verbose_name='E-mail', db_index=True)
    comment = models.TextField(verbose_name='Описание проблемы/вопроса', db_index=True)

    def __str__(self):
        return self.email
