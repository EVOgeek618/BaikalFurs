# Generated by Django 3.2.7 on 2021-11-18 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firsttry', '0013_alter_comment_topic'),
    ]

    operations = [
        migrations.AddField(
            model_name='ask',
            name='user',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Имя отправителя'),
        ),
    ]