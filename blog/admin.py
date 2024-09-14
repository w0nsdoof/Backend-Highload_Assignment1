from django.contrib import admin
from .models import Post, Comment

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('text', 'author', 'post', 'created_at')
    list_filter = ('created_at',)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    # fields = ['title', 'content', 'author']
    # exclude = ['created_at', 'updated_at']

    list_display = ('title', 'author', 'created_at')

    search_fields = ('title',)

    date_hierarchy="created_at"