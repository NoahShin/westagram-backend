# Generated by Django 3.1 on 2020-09-02 08:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_remove_users_mobile'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Users',
            new_name='Account',
        ),
    ]