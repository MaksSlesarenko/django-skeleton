from django import template
from django.db import models
from django.core.urlresolvers import reverse

register = template.Library()

@register.simple_tag
def edit_list(instance):
    
    route = instance.__class__.__name__.lower() + '_edit'

    return reverse(route, args=(instance.id,))

