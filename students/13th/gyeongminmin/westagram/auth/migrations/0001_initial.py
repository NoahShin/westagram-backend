# Generated by Django 3.1.1 on 2020-10-09 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=600)),
                ('name', models.CharField(max_length=50)),
                ('phone_number', models.CharField(max_length=20)),
            ],
        ),
    ]
