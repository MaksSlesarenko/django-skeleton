from app.students.models import Student
from django.contrib import admin


class StudentAdmin(admin.ModelAdmin):
    """Student admin model"""

admin.site.register(Student, StudentAdmin)