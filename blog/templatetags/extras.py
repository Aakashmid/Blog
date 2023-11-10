from django import template

register=template.Library()

@register.filter(name='get_replies')
def get_val(dict, key):
    return dict.get(key)