# app specific urls
from django.conf.urls import patterns, include, url
#from django.views.generic.simple import redirect_to
from django.core.urlresolvers import reverse


urlpatterns = patterns('',
    url(r'^$', 'app.task.views.home', name='task_home'),
    url(r'^add', 'app.task.views.task_add', name='task_add'),
    url(r'^list', 'app.task.views.task_list', name='task_list'),
    url(r'^delete/(\d+)', 'app.task.views.task_delete', name='task_delete'),
    url(r'^complete/(\d+)', 'app.task.views.task_complete', name='task_complete'),
    
)
