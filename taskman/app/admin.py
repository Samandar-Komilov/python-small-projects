from django.contrib import admin

from app.models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'due_date', 'reminder_interval', 'created_at', 'updated_at')
    list_display_links = ('title',)
    search_fields = ('title', 'description')
