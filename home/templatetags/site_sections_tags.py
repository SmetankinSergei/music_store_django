from django import template

from config.constants import SITE_SECTIONS

register = template.Library()


@register.simple_tag()
def get_site_sections():
    return SITE_SECTIONS


@register.simple_tag()
def is_manager(user):
    return user.groups.filter(name='managers').exists()
