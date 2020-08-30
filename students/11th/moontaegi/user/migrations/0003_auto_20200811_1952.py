# Generated by Django 3.0.8 on 2020-08-11 19:52

from django.db import migrations, models
import user.validator


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20200807_1404'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=300, validators=[user.validator.validate_password]),
        ),
    ]