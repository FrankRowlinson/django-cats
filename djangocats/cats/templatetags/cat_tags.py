from django import template
from cats.models import *


register = template.Library()


@register.simple_tag()
def get_categories(show_parameter=None):
    return Category.objects.all()
