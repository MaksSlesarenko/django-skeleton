from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.template import RequestContext

from app.students.models import Student
from app.students.forms import StudentForm

from django.template.loader import render_to_string

from django.db.models import Count

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required

import json


@login_required
def student_home(request, group_id):
    paginator = Paginator(Student.objects.filter(group__exact=group_id), 25)

    try:
        students = paginator.page(request.GET.get('page'))
    except PageNotAnInteger:
        students = paginator.page(1)
    except EmptyPage:
        students = paginator.page(paginator.num_pages)

    if request.is_ajax():
        template = 'student_list.html'
    else:
        template = 'student_home.html'

    return render_to_response(template, {'students': students, 'group_id': group_id}, context_instance=RequestContext(request))


@login_required
def student_add(request, group_id):
    if False == request.is_ajax():
        return HttpResponseRedirect(reverse('student_home'))

    form_template = ''
    success = False

    if 'POST' == request.method:
        form = StudentForm(request.REQUEST, request.FILES)
        if form.is_valid():
            student = form.save(commit=False)
            student.group_id = group_id
            student.save()

            messages.add_message(request, messages.SUCCESS, 'Added successfully.')
            success = True
        else:
            form_template = render_to_string('student_add.html', {'form': form, 'group_id': group_id})
            messages.add_message(request, messages.ERROR, 'Submited data is not valid.')
    else:
        form = StudentForm()
        form_template = render_to_string('student_add.html', {'form': form, 'group_id': group_id})

    return HttpResponse(json.dumps({'form': form_template, 'success': success}), mimetype="application/json")


@login_required
def student_edit(request, id):
    if False == request.is_ajax():
        return HttpResponseRedirect(reverse('student_home'))

    student = Student.objects.get(id=id)

    if student is None:
        return HttpResponseRedirect(reverse('group_home'))

    form_template = ''
    success = False

    if 'POST' == request.method:
        form = StudentForm(request.REQUEST, request.FILES, instance=student)
        if form.is_valid():
            form.save()

            messages.add_message(request, messages.SUCCESS, 'Added successfully.')
            success = True
        else:
            messages.add_message(request, messages.ERROR, 'Submited data is not valid.')
            form_template = render_to_string('student_edit.html', {'form': form})
    else:
        form = StudentForm(instance=student)
        form_template = render_to_string('student_edit.html', {'form': form})

    return HttpResponse(json.dumps({'form': form_template, 'success': success}), mimetype="application/json")


@login_required
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
