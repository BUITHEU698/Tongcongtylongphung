# Generated by Django 3.2.13 on 2022-05-11 15:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app2', '0022_portfoliomodel_portfolioimg'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='portfoliomodel',
            name='portfolioBody',
        ),
        migrations.RemoveField(
            model_name='portfoliomodel',
            name='portfolioName',
        ),
        migrations.RemoveField(
            model_name='portfoliomodel',
            name='portfolioPub',
        ),
        migrations.RemoveField(
            model_name='portfoliomodel',
            name='portfolioTimePub',
        ),
    ]
