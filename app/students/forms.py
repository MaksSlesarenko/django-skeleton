from django import forms
from app.students.models import Student


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        exclude = ('group',)
