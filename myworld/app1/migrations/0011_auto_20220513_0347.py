# Generated by Django 3.2.13 on 2022-05-12 20:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0010_auto_20220513_0344'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usermodel',
            old_name='LastName',
            new_name='userName',
        ),
        migrations.RemoveField(
            model_name='usermodel',
            name='FirstName',
        ),
    ]
