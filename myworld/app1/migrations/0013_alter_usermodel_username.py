# Generated by Django 3.2.13 on 2022-05-12 22:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0012_auto_20220513_0349'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodel',
            name='userName',
            field=models.CharField(default='Name', max_length=25, verbose_name='UserName'),
        ),
    ]
