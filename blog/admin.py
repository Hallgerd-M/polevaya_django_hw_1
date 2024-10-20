from django.contrib import admin

from blog.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("id", "heading", "content", "views_counter")
    search_fields = ("heading", "views_counter")
