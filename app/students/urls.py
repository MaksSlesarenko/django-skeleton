from django.conf.urls import patterns, include, url
from django.core.urlresolvers import reverse


urlpatterns = patterns(
    '',
    url(r'^(\d+)$', 'app.students.views.student_home', name='student_home'),
    url(r'^(\d+)/list', 'app.students.views.student_list', name='student_list'),
    url(r'^(\d+)/add', 'app.students.views.student_add', name='student_add'),
    url(r'^(\d+)/edit', 'app.students.views.student_add', name='student_edit'),
    url(r'^(\d+)/delete', 'app.students.views.student_delete', name='student_delete'),
)
