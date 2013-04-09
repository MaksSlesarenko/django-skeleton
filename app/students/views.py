from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib import messages

from app.students.models import Student
from app.students.forms import StudentForm, StudentEditForm

from django.template.loader import render_to_string

from django.db.models import Count

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

import json


def student_home(request, group_id):
    paginator = Paginator(Student.objects.filter(group__exact=group_id), 25)

    try:
        students = paginator.page(request.GET.get('page'))
    except PageNotAnInteger:
        students = paginator.page(1)
    except EmptyPage:
        students = paginator.page(paginator.num_pages)

    return render_to_response('student_home.html', {'students': students, 'group_id': group_id })


def student_list(request, group_id):

    paginator = Paginator(Student.objects.filter(group__exact=group_id), 25)
    
    try:
        students = paginator.page(request.GET.get('page'))
    except PageNotAnInteger:
        students = paginator.page(1)
    except EmptyPage:
        students = paginator.page(paginator.num_pages)

    return render_to_response('student_list.html', {'students': students})

def student_add(request, group_id):
    form_template = ''
    success = False

    if request.is_ajax():
        if 'POST' == request.method:
            form = StudentForm(request.REQUEST, request.FILES, instance=Student(group_id=group_id))
            if form.is_valid():
                form.save()
                
                messages.add_message(request, messages.SUCCESS, 'Added successfully.')
                success = True
            else:
                form_template = render_to_string('student_add.html', { 'form': form , 'group_id': group_id })
                messages.add_message(request, messages.ERROR, 'Submited data is not valid.')
        else:
            form_template = render_to_string('student_add.html', { 'form': StudentForm(instance=Student(group_id=group_id)), 'group_id': group_id })
    else:
        return HttpResponseRedirect(reverse('student_home'))

    return HttpResponse(json.dumps({'form': form_template, 'success': success}), mimetype="application/json")


def student_edit(request, id):
    form_template = ''
    success = False

    if request.is_ajax():
        if 'POST' == request.method:
            form = StudentEditForm(request.REQUEST, request.FILES)
            if form.is_valid():
                student = Student(name=form.cleaned_data['name'])
                student.save()
                
                messages.add_message(request, messages.SUCCESS, 'Added successfully.')
                success = True
            else:
                messages.add_message(request, messages.ERROR, 'Submited data is not valid.')
                form_template = render_to_string('student_edit.html', { 'form': form, 'id': id })
        else:
            form_template = render_to_string('student_edit.html', { 'form': studentEditForm(), 'id': id })
    else:
        return HttpResponseRedirect(reverse('student_home'))

    return HttpResponse(json.dumps({'form': form_template, 'success': success}), mimetype="application/json")


def student_delete(request, id):

    if request.is_ajax():
        student = Student.objects.get(id=id)

        if (student):
            student.delete()
            messages.add_message(request, messages.SUCCESS, 'Deleted successfully.')
            result = True
        else:
            messages.add_message(request, messages.ERROR, 'Submited data is not valid.')
            result = False
    else:
        return HttpResponseRedirect(reverse('student_home'))

    return HttpResponse(json.dumps({'result': result}), mimetype="application/json")
