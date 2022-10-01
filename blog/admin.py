from django.contrib import admin
from markdownx.admin import MarkdownxModelAdmin

from .models import Category, Tag, Post


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('display_order', 'name', 'slug')
    list_display_links = ('name',)
    ordering = ('display_order', 'slug')
    search_fields = ('name',)


class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    list_display_links = ('name',)
    search_fields = ('name',)


class PostAdmin(MarkdownxModelAdmin):
    exclude = ('bookmarked', 'page_views')
    list_display = (
        'title', 'slug', 'category', 'keywords',
        'created_at', 'published_at', 'updated_at'
    )
    list_display_links = ('title',)
    list_filter = ('is_published',)
    search_fields = ('title',)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Post, PostAdmin)
