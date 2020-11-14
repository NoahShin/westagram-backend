# Generated by Django 3.1.3 on 2020-11-13 04:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('posting', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Accounts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=300)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'accounts',
            },
        ),
        migrations.CreateModel(
            name='Broadlikes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='user.accounts')),
                ('broad', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='posting.broads')),
            ],
            options={
                'db_table': 'accounts_borads',
            },
        ),
    ]
