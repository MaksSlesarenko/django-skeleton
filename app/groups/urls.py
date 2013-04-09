from django.conf.urls import patterns, include, url
from django.core.urlresolvers import reverse


urlpatterns = patterns(
    '',
    url(r'^$', 'app.groups.views.group_home', name='group_home'),
    url(r'^list', 'app.groups.views.group_list', name='group_list'),
    url(r'^add', 'app.groups.views.group_add', name='group_add'),
    url(r'^(\d+)/edit', 'app.groups.views.group_edit', name='group_edit'),
    url(r'^(\d+)/delete', 'app.groups.views.group_delete', name='group_delete'),
)
