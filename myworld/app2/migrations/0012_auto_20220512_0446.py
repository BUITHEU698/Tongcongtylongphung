# Generated by Django 3.2.13 on 2022-05-11 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app2', '0011_auto_20220512_0215'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfoliomodel',
            name='portfolioTimePub',
            field=models.DateTimeField(verbose_name='Thời gian hiển thị'),
        ),
        migrations.AlterField(
            model_name='productsmodel',
            name='productsTimePub',
            field=models.DateTimeField(verbose_name='Thời gian hiển thị'),
        ),
    ]
