from django.shortcuts import render_to_response
from myfirstapp.models import Task

def home(request):

    params = {}
    params["tasks"] = Task.objects.all()
    return render_to_response('home.html', params)

def add_task(request):
    #print dir(GET)
    
    new_title = request.GET.get('title', '')
    if new_title:
        task = Task(title=new_title)
        task.save()
    
    params = {}
    params["tasks"] = Task.objects.all()
    
    return render_to_response('tasks.html', params);
