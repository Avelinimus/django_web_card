from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.


class Index(models.Model):
    pass


class Contact(models.Model):

    class Meta:
        ordering = ['title']
        verbose_name = 'Описание для контактов'
        verbose_name_plural = 'Описание для контактов'

    title = models.CharField(max_length=100, db_index=True, verbose_name='Название')
    description = RichTextUploadingField(blank=True, verbose_name='Описание')

    def __str__(self):
        return self.title