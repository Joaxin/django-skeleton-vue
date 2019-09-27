from django.contrib import admin
from .models import Message, Category

# Register your models here.
@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'created', 'updated','content','category',)
    list_filter = ('author', 'created', 'category')
    search_fields = ('category', 'content')
    date_hierarchy = 'created'
    ordering = ('updated',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    rdering = ('name',)