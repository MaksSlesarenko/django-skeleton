# app specific urls
from django.conf.urls import patterns, include, url
#from django.views.generic.simple import redirect_to
from django.core.urlresolvers import reverse


urlpatterns = patterns('',
    url(r'^home', 'myfirstapp.views.home', name='home'),
    url(r'^task/add', 'myfirstapp.views.task_add', name='task_add'),
    url(r'^task/list', 'myfirstapp.views.task_list', name='task_list'),
    url(r'^task/delete/(\d+)', 'myfirstapp.views.task_delete', name='task_delete'),
    url(r'^task/complete/(\d+)', 'myfirstapp.views.task_complete', name='task_complete'),
)
