# Generated by Django 3.2.13 on 2022-05-11 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app2', '0003_alter_portfoliomodel_portfoliopub'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfoliomodel',
            name='portfolioPub',
            field=models.CharField(choices=[('1', 'Ẩn'), ('2', 'Hiện')], default='2', max_length=250),
        ),
    ]