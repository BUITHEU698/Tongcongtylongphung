# Generated by Django 4.0.2 on 2022-05-10 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PortfolioModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('portfolioName', models.CharField(max_length=200)),
                ('portfolioTimePub', models.DateTimeField()),
                ('portfolioBody', models.TextField()),
                ('portfolioImg', models.FileField(upload_to='')),
            ],
        ),
    ]