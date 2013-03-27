from django.db import models

# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=255)
    create_date = models.DateTimeField(auto_now_add = True)
    #update_date = models.DateField()