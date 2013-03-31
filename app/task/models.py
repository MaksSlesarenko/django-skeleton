from django.db import models
from datetime import datetime
from django.contrib import admin


class Task(models.Model):
    """Task model"""

    title = models.CharField(max_length=255)
    create_date = models.DateTimeField(auto_now_add=True)
    complete_date = models.DateTimeField(null=True)

    def complete(self):
        """Mark task as complete"""

        self.complete_date = datetime.now()
        self.save()

    def is_complete(self):
        """Check if task is complete"""

        return self.complete_date is not None


class TaskAdmin(admin.ModelAdmin):
    """Task admin model"""

admin.site.register(Task, TaskAdmin)
