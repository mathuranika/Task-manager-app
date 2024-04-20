from django.contrib import admin
from .models import TodoItem

class TodoItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'completed')

#Register the model
admin.site.register(TodoItem, TodoItemAdmin)
