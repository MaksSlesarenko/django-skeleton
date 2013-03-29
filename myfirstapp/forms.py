from django import forms

# Create your models here.

class TaskForm(forms.Form):
    title = forms.CharField(max_length=255)
