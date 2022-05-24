# Generated by Django 3.2.13 on 2022-05-23 22:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app2', '0020_auto_20220524_0331'),
        ('app1', '0015_remove_ordermodel_completed_remove_ordermodel_user_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CartItemHistoryModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantile', models.IntegerField(default=0, verbose_name='Số lượng')),
                ('products', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app2.productsmodel')),
            ],
        ),
    ]