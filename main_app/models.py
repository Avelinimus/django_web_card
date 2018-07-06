from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


# Create your models here.
from django.urls import reverse


class Index(models.Model):
    class Meta:
        ordering = ['title']
        verbose_name = 'Описание на главной странице'
        verbose_name_plural = 'Описание на главной странице'

    title = models.CharField(max_length=100, db_index=True, verbose_name='Название')
    description = RichTextUploadingField(blank=True, verbose_name='Описание')

    def __str__(self):
        return self.title


class Services(models.Model):
    class Meta:
        ordering = ['name']
        verbose_name = 'Услугу'
        verbose_name_plural = 'Услуги'

    name = models.CharField(max_length=100, db_index=True, verbose_name='Название типа сайта')
    slug = models.SlugField(max_length=200, db_index=True,
                            unique=True, help_text='Нужно использовать для создания "хороших" URL-ов')
    price = models.price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена(грн)")
    description = RichTextUploadingField(blank=True, verbose_name='Описание')
    image = models.ImageField(upload_to='products/img/%Y/%m/%d/', blank=True,
                              verbose_name="Картинка для услуги(300 x 300)")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('main_app:service_detail', args={self.slug})


class Contact(models.Model):
    class Meta:
        ordering = ['title']
        verbose_name = 'Описание для контактов'
        verbose_name_plural = 'Описание для контактов'

    title = models.CharField(max_length=100, db_index=True, verbose_name='Название')
    description = RichTextUploadingField(blank=True, verbose_name='Описание')

    def __str__(self):
        return self.title


class FAQ(models.Model):
    class Meta:
        ordering = ['section']
        verbose_name = 'Вопрос/Ответ'
        verbose_name_plural = 'Вопросы/Ответы'

    section = models.CharField(max_length=100, db_index=True, verbose_name='Название')
    description = RichTextUploadingField(blank=True, verbose_name='Описание')

    def __str__(self):
        return self.section
