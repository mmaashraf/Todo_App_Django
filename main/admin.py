from django.contrib import admin

# Register your models here.
from .models import MainTodo
from django.db import models
# Register your models here.

class TodoAdmin(admin.ModelAdmin):
    fieldsets=[
    ("username/Title/deadline",{"fields":["todo_username","todo_title","todo_deadline"]}),
    ("status",{"fields":["todo_status"]}),
    ("Content",{"fields":["todo_content"]})
    ]

admin.site.register(MainTodo,TodoAdmin)
