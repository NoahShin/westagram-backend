# Generated by Django 3.0.3 on 2020-08-04 00:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, null=True, unique=True)),
                ('email', models.EmailField(max_length=254, null=True, unique=True)),
                ('phone', models.CharField(max_length=30, null=True, unique=True)),
                ('password', models.CharField(max_length=40)),
            ],
            options={
                'db_table': 'users',
            },
        ),
    ]
