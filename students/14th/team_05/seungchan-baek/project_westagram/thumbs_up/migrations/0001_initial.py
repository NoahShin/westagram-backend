# Generated by Django 3.1.3 on 2020-11-11 17:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('post', '0003_auto_20201110_2337'),
        ('user', '0009_auto_20201111_1610'),
    ]

    operations = [
        migrations.CreateModel(
            name='ThumbsUp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='post.posting')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.user')),
            ],
            options={
                'db_table': 'thumbs_up',
            },
        ),
    ]