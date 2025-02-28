from django import template
from ..models import Brands, Colors

register = template.Library()

@register.simple_tag
def get_brands():
    return Brands.objects.all()

@register.simple_tag
def get_colors():
    return Colors.objects.all()
