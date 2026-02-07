from django import template

register = template.Library()


@register.filter
def split(value, arg):
    """Split string by given separator."""
    if not value:
        return []
    return value.split(arg)
