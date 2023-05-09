from django import template
from store.models import *

register = template.Library()

@register.simple_tag(name='getarts')
def get_articles():
    return Articles.objects.all