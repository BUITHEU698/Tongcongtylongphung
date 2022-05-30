# Generated by Django 4.0.4 on 2022-05-30 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0019_ordermodel_odertime'),
    ]

    operations = [
        migrations.CreateModel(
            name='Snippet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=225)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('body', models.TextField()),
            ],
        ),
    ]
