# Generated by Django 3.1.3 on 2020-11-08 07:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posting', '0002_auto_20201108_1458'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='email',
            new_name='user',
        ),
    ]