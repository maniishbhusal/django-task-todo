from django.contrib import admin
from .models import TodoItem

class TodoItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'completed')
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(TodoItem, TodoItemAdmin)