# Generated by Django 3.2.13 on 2022-05-12 09:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app2', '0013_remove_productsmodel_portfoliomodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='productsmodel',
            name='portfolioModel',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app2.portfoliomodel'),
            preserve_default=False,
        ),
    ]
