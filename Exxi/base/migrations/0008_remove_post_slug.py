# Generated by Django 4.2.7 on 2023-11-24 01:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_post_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='slug',
        ),
    ]