# Generated by Django 3.1 on 2020-09-03 23:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20200902_1116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='email',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='users',
            name='phone_number',
            field=models.CharField(max_length=12, null=True),
        ),
    ]