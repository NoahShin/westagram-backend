# Generated by Django 3.1.1 on 2020-10-15 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0013_auto_20201015_1523'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='following',
            field=models.ManyToManyField(related_name='follows', through='user.Follow', to='user.User'),
        ),
    ]
