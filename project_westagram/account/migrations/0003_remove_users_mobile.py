# Generated by Django 3.1 on 2020-09-02 07:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_users_mobile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='mobile',
        ),
    ]