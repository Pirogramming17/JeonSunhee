from django.contrib import admin
from .models import Post, Devtool, IdeaStart

# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass

@admin.register(Devtool)
class DevtoolAdmin(admin.ModelAdmin):
    pass


# @admin.register(User)
# class UserAdmin(admin.ModelAdmin):
#     pass

# class PostResource(resources.ModelResource):
#     class Meta:
#         model = Post
#         fields = ('id', 'title', 'user', 'content', 'price', 'region', 'photo')
#         export_order = fields

# class PostAdmin(ImportExportModelAdmin):
#     fields = ('title', 'user', 'content', 'price', 'region', 'photo')
#     list_display = ('id', 'title', 'user', 'content', 'price', 'region', 'photo')
#     resource_class = PostResource

# admin.site.register(Post, PostAdmin)