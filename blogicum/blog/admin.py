from django.contrib import admin
from django.db import models
from django.forms import Textarea

from .models import Category, Location, Post

admin.site.empty_value_display = 'Не задано'


class PostInLine(admin.StackedInline):
    model = Post
    extra = 0


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    inlines = (
        PostInLine,
    )
    list_display = (
        'title',
        'description',
    )


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows': 5, 'cols': 50})},
    }  # уменьшил поле текста сообщения для лучшего восприятия
    list_display = (
        'is_published',
        'author',
        'category',
        'title',
        'location',
        'text',
        'pub_date',
    )
    list_editable = (
        'category',
        'text',
        'is_published',
    )
    search_fields = ('title', 'text', 'category')
    list_filter = ('category',)
    list_display_links = ('title',)


admin.site.register(Location)
