from django import template
from cats.models import *


register = template.Library()


@register.simple_tag()
def get_categories(show_parameter=None):
    categories = {
        None: Category.objects.all(),
        'count': Category.objects.count(),
        'names': [category.name for category in Category.objects.order_by('name')],
    }
    if show_parameter in categories:
        return categories[show_parameter]