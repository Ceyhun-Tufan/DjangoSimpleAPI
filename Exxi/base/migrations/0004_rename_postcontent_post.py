# Generated by Django 4.2.7 on 2023-11-19 19:40

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('base', '0003_comment_delete_comments'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='PostContent',
            new_name='Post',
        ),
    ]