from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    # fields = ['title', 'content', 'author']
    # exclude = ['created_at', 'updated_at']

    list_display = ('title', 'author', 'created_at')

    search_fields = ('title',)

    date_hierarchy="created_at"