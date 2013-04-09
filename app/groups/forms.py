from django import forms
from app.students.models import Student


class GroupForm(forms.Form):
    name = forms.CharField(max_length=255)

class GroupEditForm(GroupForm):
    lead = forms.ModelChoiceField(queryset = Student.objects.all())