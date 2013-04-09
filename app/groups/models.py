from django.db import models
from datetime import datetime

class Group(models.Model):
    """Group model"""

    name = models.CharField(max_length=255)
    lead = models.ForeignKey('students.Student', related_name='group_to_user', null=True, on_delete=models.SET_NULL)
