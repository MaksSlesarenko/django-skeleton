from app.task.models import Task
from django.contrib import admin


class TaskAdmin(admin.ModelAdmin):
    """Task admin model"""

admin.site.register(Task, TaskAdmin)
