from django.contrib import messages
from django.contrib import auth
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response
from django.template import RequestContext


from django.contrib.auth.decorators import login_required

@login_required()
def profile(request):
    return render_to_response('profile.html', context_instance=RequestContext(request))
    
@login_required()
def logout(request):
    auth.logout(request)
    
    messages.add_message(request, messages.SUCCESS, 'Logout successful.')
    return HttpResponseRedirect(reverse('task_home'))