# Generated by Django 2.0.7 on 2018-07-08 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms_app', '0002_auto_20180707_1908'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'ordering': ['email'], 'verbose_name': 'Заказ', 'verbose_name_plural': 'Заказы'},
        ),
        migrations.AlterModelOptions(
            name='support',
            options={'ordering': ['email'], 'verbose_name': 'Сообщение поддержки', 'verbose_name_plural': 'Сообщения поддержки'},
        ),
        migrations.AddField(
            model_name='order',
            name='flag',
            field=models.BooleanField(default=False, verbose_name='Отправить сообщение вам на почту?'),
        ),
        migrations.AlterField(
            model_name='order',
            name='email',
            field=models.EmailField(db_index=True, max_length=30, verbose_name='E-mail'),
        ),
        migrations.AlterField(
            model_name='order',
            name='time',
            field=models.CharField(blank=True, default='Не важно', max_length=30, verbose_name='Удобное для вас время'),
        ),
    ]
