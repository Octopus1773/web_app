from django.contrib import admin
from .models import *

class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_create', 'photo', 'get_content', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title',)
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_create')

    def get_content(self, obj):
        return ', '.join([ content.content_text for content in obj.content.all()])


class ContentAdmin(admin.ModelAdmin):
    list_display = ('id',)
    list_display_links = ('id',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')


admin.site.register(Post, PostAdmin)
admin.site.register(Content, ContentAdmin)
admin.site.register(Category)





