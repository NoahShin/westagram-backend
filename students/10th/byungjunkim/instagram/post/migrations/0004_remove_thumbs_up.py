# Generated by Django 3.0.8 on 2020-07-13 04:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0003_thumbs'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='thumbs',
            name='up',
        ),
    ]
