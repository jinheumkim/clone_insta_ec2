# Generated by Django 4.2.6 on 2023-10-10 08:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feed',
            name='like_count',
        ),
    ]
