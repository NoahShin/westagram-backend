# Generated by Django 3.0.8 on 2020-08-05 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Posting', '0003_auto_20200805_1339'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='img_url',
            field=models.URLField(default=''),
        ),
    ]