from django.contrib import admin
from .models import Post, Reply
# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass

@admin.register(Reply)
class ReplyAdmin(admin.ModelAdmin):
    pass