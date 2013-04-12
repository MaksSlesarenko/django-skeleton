from django.db import models
from datetime import datetime
from app.groups.models import Group
from django.db.models.signals import post_save, post_delete

import logging


class Student(models.Model):
    """Studen model"""

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d')
    birthday = models.DateField(null=True)

    uid = models.CharField(max_length=255)
    group = models.ForeignKey('groups.Group', related_name='user_to_group', null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class StudentLog(models.Model):
    """Studen model"""

    created_at = models.DateTimeField(auto_now_add=True)
    is_created = models.NullBooleanField()
    is_deleted = models.NullBooleanField()
    student_id = models.IntegerField()


def student_save_logger(sender, **kwargs):
    log = StudentLog()
    log.student_id = kwargs['instance'].id
    log.is_created = kwargs['created']
    log.save()


def student_delete_logger(sender, **kwargs):
    log = StudentLog()
    log.student_id = kwargs['instance'].id
    log.is_deleted = True
    log.save()


post_save.connect(student_save_logger, sender=Student)
post_delete.connect(student_delete_logger, sender=Student)
