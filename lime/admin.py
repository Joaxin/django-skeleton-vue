from django.contrib import admin
from .models import Bookmark, Category

# Register your models here.
@admin.register(Bookmark)
class BookmarkAdmin(admin.ModelAdmin):
    list_display = ('title', 'url', 'author', 'created', 'pub_date',)
    list_filter = ('title', 'author', 'url', 'is_public',)
    search_fields = ('title', 'url',)
    date_hierarchy = 'pub_date'
    ordering = ('pub_date',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    rdering = ('name',)