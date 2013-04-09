from app.task.models import Group
from django.contrib import admin


class GroupAdmin(admin.ModelAdmin):
    """Group admin model"""

admin.site.register(Group, GroupAdmin)
