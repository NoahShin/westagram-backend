# Generated by Django 3.1.1 on 2020-09-10 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_auto_20200910_1434'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='user',
            name='phon_number',
            field=models.CharField(max_length=100),
        ),
    ]
