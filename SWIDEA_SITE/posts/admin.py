from django.contrib import admin
from .models import Post, Devtool, IdeaStart

# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass
