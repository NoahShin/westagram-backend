# Generated by Django 3.1.1 on 2020-10-13 22:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0011_auto_20201013_2237'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='following',
            field=models.ManyToManyField(through='user.Follow', to='user.User'),
        ),
    ]
