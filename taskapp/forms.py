from django import forms

class TaskForm(forms.Form):
    title = forms.CharField(max_length=255)
