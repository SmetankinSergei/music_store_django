from django import template

from mail_service.constants import MAILING_SERVICES, WEEK_DAYS, MONTHS_DAYS
from mail_service.models import Recipient, MailContent
from mail_service.session import session

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


@register.simple_tag()
def get_week_days():
    return WEEK_DAYS


@register.simple_tag()
def get_months_days():
    return MONTHS_DAYS


@register.simple_tag()
def get_session_week_days():
    return session.week_days


@register.simple_tag()
def get_session_month_days():
    return session.months_days


@register.simple_tag()
def mailing_done():
    if session.letter and session.recipients_list and session.mailing_time:
        if session.mailing_type != 'ONE_TIME':
            if session.week_days or session.months_days:
                return True
            else:
                return False
        return True
