# Generated by Django 3.2.7 on 2021-12-06 10:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('firsttry', '0016_userinfo'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userinfo',
            options={'verbose_name': 'Профиль', 'verbose_name_plural': 'Профили'},
        ),
    ]