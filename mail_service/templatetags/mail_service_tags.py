from django import template

from mail_service.constants import MAILING_SERVICES, WEEK_DAYS, MONTHS_DAYS
from mail_service.models import Recipient, MailContent, Mailing
from mail_service.session import session
from users.models import User

register = template.Library()


@register.simple_tag()
def get_mail_services_list():
    return MAILING_SERVICES


@register.simple_tag()
def get_recipients_list():
    return Recipient.objects.all()


@register.simple_tag()
def get_current_recipients():
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
def get_mailings(user):
    return Mailing.objects.filter(owner=user)


@register.simple_tag()
def mailing_done():
    if session.letter and session.recipients_list and session.mailing_time:
        if session.mailing_type != 'ONE_TIME':
            if session.week_days or session.months_days:
                return True
            else:
                return False
        return True


@register.simple_tag()
def get_active_mailings_amount(user):
    return len(Mailing.objects.filter(owner=user, status__in=['CREATED', 'IN_PROGRES']))


@register.simple_tag()
def get_unique_clients_amount(user):
    mailings = Mailing.objects.filter(owner=user)
    return sum([len(get_mailing_recipients_list(mailing)) for mailing in mailings])


def get_mailing_recipients_list(mailing):
    return mailing.recipients.all()


@register.simple_tag()
def get_all_mailings():
    return Mailing.objects.all()


@register.simple_tag()
def get_all_clients():
    return User.objects.all()
