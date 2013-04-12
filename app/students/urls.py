from django.conf.urls import patterns, include, url
from django.core.urlresolvers import reverse


urlpatterns = patterns(
    '',
    url(r'^group/(\d+)$', 'app.students.views.student_home', name='student_home'),
    url(r'^group/(\d+)/add', 'app.students.views.student_add', name='student_add'),
    url(r'^(\d+)/edit', 'app.students.views.student_edit', name='student_edit'),
    url(r'^(\d+)/delete', 'app.students.views.student_delete', name='student_delete'),
)
