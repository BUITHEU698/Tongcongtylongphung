# Generated by Django 4.0.4 on 2022-05-24 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0015_remove_ordermodel_completed_remove_ordermodel_user_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordermodel',
            name='tongCong',
            field=models.IntegerField(default=0, verbose_name='Tong tien hoa don'),
        ),
    ]
