# Generated by Django 3.2.13 on 2022-05-11 07:19

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app2', '0006_auto_20220511_1417'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfoliomodel',
            name='portfolioTimePub',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Start Date'),
        ),
    ]
