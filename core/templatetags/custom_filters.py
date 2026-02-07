from django import template

register = template.Library()


@register.filter
def split(value, arg):
    """Split string by given separator."""
    if not value:
        return []
    return value.split(arg)


@register.filter
def trim(value):
    """Trim leading/trailing whitespace from a string."""
    if value is None:
        return ""
    return str(value).strip()
