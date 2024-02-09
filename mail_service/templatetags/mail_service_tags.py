from django import template

from mail_service.constants import MAILING_SERVICES


register = template.Library()


@register.simple_tag()
def get_mail_services_list():
    return MAILING_SERVICES
