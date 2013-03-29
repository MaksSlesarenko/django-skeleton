from django.shortcuts import render_to_response
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib import messages

from myfirstapp.models import Task
from myfirstapp.forms import TaskForm

import json

def home(request):

    params = {}
    params["tasks"] = Task.objects.all()
    params['form'] = TaskForm()
    
    return render_to_response('home.html', params)

def task_list(request):
    
    return render_to_response('tasks.html', {'tasks': Task.objects.all()})

def task_delete(request, id):
    
    if request.is_ajax():
        task = Task.objects.get(id=id)
        
        if (task):
            task.delete()
            messages.add_message(request, messages.SUCCESS, 'Deleted successfully.')
            result = 1
        else:
            messages.add_message(request, messages.ERROR, 'Submited data is not valid.')
            result = 0
    else:
        return HttpResponseRedirect('/404/')
        
    return HttpResponse(json.dumps({'result': result}), mimetype="application/json")

def task_complete(request, id):
    
    if request.is_ajax():
        task = Task.objects.get(id=id)
        
        if (task):
            task.complete()
            messages.add_message(request, messages.SUCCESS, 'Marked as completed successfully.')
            result = 1
        else:
            messages.add_message(request, messages.ERROR, 'Submited data is not valid.')
            result = 0
    else:
        return HttpResponseRedirect('/404/')
        
    return HttpResponse(json.dumps({'result': result}), mimetype="application/json")


def task_add(request):

    if request.is_ajax():
        form = TaskForm(request.REQUEST)
        
        if form.is_valid(): # All validation rules pass
            task = Task(title=form.cleaned_data['title'])
            task.save()
            messages.add_message(request, messages.SUCCESS, 'Added successfully.')
            result = 1
        else:
            messages.add_message(request, messages.ERROR, 'Submited data is not valid.')
            result = 0
    else:
        return HttpResponseRedirect('/404/')
        
    return HttpResponse(json.dumps({'result': result}), mimetype="application/json")
