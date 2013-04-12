from django import forms
from app.students.models import Student
from app.groups.models import Group


class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        exclude = ('lead',)


class GroupEditForm(GroupForm):
    class Meta:
        model = Group

    def __init__(self, *args, **kwargs):
        super(GroupEditForm, self).__init__(*args, **kwargs)

        students = Student.objects.filter(group_id=self.instance.id)
        
        self.fields['lead'].queryset = students
        if len(students) < 1:
            self.fields['lead'].required = False
