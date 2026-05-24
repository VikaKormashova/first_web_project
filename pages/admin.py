from django.contrib import admin
from .models import Idea

@admin.register(Idea)
class IdeaAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'budget', 'author', 'duration_hours', 'is_active', 'created_at')
    list_filter = ('category', 'budget', 'is_active', 'author', 'created_at')
    search_fields = ('title', 'description', 'author__username')
    list_editable = ('is_active',)
    readonly_fields = ('created_at', 'updated_at')
    
    fieldsets = (
        ('Основная информация', {
            'fields': ('title', 'description', 'category', 'budget')
        }),
        ('Дополнительно', {
            'fields': ('image_url', 'duration_hours', 'is_active', 'author')
        }),
        ('Даты', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )