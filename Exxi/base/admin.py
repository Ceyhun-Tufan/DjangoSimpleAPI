from django.contrib import admin
from .models import Topic,Post,Comment
from django.contrib.auth.admin import UserAdmin

# Register your models here.

admin.site.register(Topic)
admin.site.register(Post)
admin.site.register(Comment)

