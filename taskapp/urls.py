# app specific urls
from django.conf.urls import patterns, include, url
#from django.views.generic.simple import redirect_to
from django.core.urlresolvers import reverse


urlpatterns = patterns('',
    url(r'^$', 'taskapp.views.home', name='task_home'),
    url(r'^add', 'taskapp.views.task_add', name='task_add'),
    url(r'^list', 'taskapp.views.task_list', name='task_list'),
    url(r'^delete/(\d+)', 'taskapp.views.task_delete', name='task_delete'),
    url(r'^complete/(\d+)', 'taskapp.views.task_complete', name='task_complete'),
    
)
