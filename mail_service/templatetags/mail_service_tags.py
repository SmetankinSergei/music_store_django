from django import template

from mail_service.constants import MAILING_SERVICES
from mail_service.models import Recipient, MailContent

register = template.Library()


@register.simple_tag()
def get_mail_services_list():
    return MAILING_SERVICES


@register.simple_tag()
def get_recipients_list():
    return Recipient.objects.all()


@register.simple_tag()
def get_current_recipients(session):
    return session.recipients_list


@register.simple_tag()
def get_letters():
    return MailContent.objects.all()
