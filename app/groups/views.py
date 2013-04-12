from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from app.groups.models import Group
from app.groups.forms import GroupForm, GroupEditForm

from django.template.loader import render_to_string

from django.db.models import Count

import json


@login_required
def group_home(request):
    request.sql_profiler = "asdasdasdasd"
    groups = Group.objects.annotate(num_students=Count('user_to_group'))

    if request.is_ajax():
        template = 'group_list.html'
    else:
        template = 'group_home.html'
    return render_to_response(template, {'groups': groups})


@login_required
def group_add(request):
    if request.is_ajax() is False:
        return HttpResponseRedirect(reverse('group_home'))

    form_template = ''
    success = False

    if 'POST' == request.method:
        form = GroupForm(request.REQUEST)
        if form.is_valid():
            group = Group(name=form.cleaned_data['name'])
            group.save()

            messages.add_message(request, messages.SUCCESS, 'Added successfully.')
            success = True
        else:
            form_template = render_to_string('group_add.html', {'form': form})
            messages.add_message(request, messages.ERROR, 'Submited data is not valid.')
    else:
        form_template = render_to_string('group_add.html', {'form': GroupForm()})

    return HttpResponse(json.dumps({'form': form_template, 'success': success}), mimetype="application/json")


@login_required
def group_edit(request, id):
    if request.is_ajax() is False:
        return HttpResponseRedirect(reverse('group_home'))

    form_template = ''
    success = False

    group = Group.objects.get(id=id)

    if group is None:
        return HttpResponseRedirect(reverse('group_home'))

    if 'POST' == request.method:
        form = GroupEditForm(request.REQUEST, instance=group)
        if form.is_valid():
            form.save()

            messages.add_message(request, messages.SUCCESS, 'Added successfully.')
            success = True
        else:
            messages.add_message(request, messages.ERROR, 'Submited data is not valid.')
            form_template = render_to_string('group_edit.html', {'form': form})
    else:
        form = GroupEditForm(instance=group)
        form_template = render_to_string('group_edit.html', {'form': form})

    return HttpResponse(json.dumps({'form': form_template, 'success': success}), mimetype="application/json")


@login_required
def group_delete(request, id):

    if request.is_ajax():
        group = Group.objects.get(id=id)

        if (group):
            group.delete()
            messages.add_message(request, messages.SUCCESS, 'Deleted successfully.')
            result = True
        else:
            messages.add_message(request, messages.ERROR, 'Submited data is not valid.')
            result = False
    else:
        return HttpResponseRedirect(reverse('group_home'))

    return HttpResponse(json.dumps({'result': result}), mimetype="application/json")
