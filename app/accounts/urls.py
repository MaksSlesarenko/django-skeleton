# app specific urls
from django.conf.urls import patterns, include, url
#from django.views.generic.simple import redirect_to
from django.core.urlresolvers import reverse


urlpatterns = patterns(
    '',
    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', 'app.accounts.views.logout', name='logout'),
    url(r'^profile/$', 'app.accounts.views.profile', name='accounts_profile'),
)
