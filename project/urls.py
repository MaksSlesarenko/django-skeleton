from django.conf.urls import patterns, include, url
from django.views.generic import RedirectView
from django.core.urlresolvers import reverse
from django.contrib import admin

admin.autodiscover()

import settings
import app.task.urls
import app.accounts.urls
import app.students.urls
import app.groups.urls

urlpatterns = patterns(
    '',

    # urls specific to this app
    url(r'^task/', include(app.task.urls)),
    url(r'^accounts/', include(app.accounts.urls)),
    url(r'^students/', include(app.students.urls)),
    url(r'^groups/', include(app.groups.urls)),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^admin/', include(admin.site.urls)),

    # catch all, redirect to taskapp home view
    url(r'^$', RedirectView.as_view(url='/task')),

    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),

)
