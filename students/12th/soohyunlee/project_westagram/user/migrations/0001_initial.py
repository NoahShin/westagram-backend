# Generated by Django 3.0.3 on 2020-09-01 08:43

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
                ('name', models.CharField(max_length=50)),
                ('phone_num', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=100)),
                ('pw', models.CharField(max_length=200)),
            ],
        ),
    ]
