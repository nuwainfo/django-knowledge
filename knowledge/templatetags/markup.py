from django.template import Library
from django_markup.markup import formatter
from django.utils.safestring import mark_safe

register = Library()

@register.filter
def markdown(text):
    return mark_safe(formatter(text, "markdown"))