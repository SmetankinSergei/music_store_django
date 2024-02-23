from mail_service.constants import WEEK_DAYS, MONTHS_DAYS
from mail_service.models import Recipient, MailContent
from mail_service.session import session
from mail_service.templatetags.mail_service_tags import get_recipients_list


def recipient_handler(request):
    action = request.GET.get('action')
    if action == 'add':
        recipient_pk = request.GET.get('recipient_pk')
        recipient = Recipient.objects.get(pk=recipient_pk)
        session.recipients_list.append(recipient)
    elif action == 'remove':
        recipient_pk = request.GET.get('recipient_pk')
        recipient = Recipient.objects.get(pk=recipient_pk)
        session.recipients_list.remove(recipient)
    elif action == 'add_all':
        session.recipients_list = list(get_recipients_list())
    elif action == 'remove_all':
        session.recipients_list = []
    return action


def letter_handler(request):
    if request.GET.get('show_letter'):
        letter = MailContent.objects.get(pk=request.GET.get('show_letter'))
        session.show_letters_list.append(letter)

    if request.GET.get('hide_letter'):
        letter = MailContent.objects.get(pk=request.GET.get('hide_letter'))
        session.show_letters_list.remove(letter)

    if request.GET.get('add_letter'):
        session.letter = MailContent.objects.get(pk=request.GET.get('add_letter'))

    if request.GET.get('remove_letter'):
        session.letter = None


def period_handler(request):
    if request.GET.get('month_day'):
        day = int(request.GET.get('month_day'))
        if day not in session.months_days:
            session.months_days.append(day)
        else:
            session.months_days.remove(day)

    if request.GET.get('week_day'):
        day = request.GET.get('week_day')
        if day not in session.week_days:
            session.week_days.append(day)
        else:
            session.week_days.remove(day)

    if request.GET.get('action') == 'add_all_days':
        if session.mailing_type == 'WEEK_DAY':
            session.week_days.extend(WEEK_DAYS)
        elif session.mailing_type == 'MONTH_DAY':
            session.months_days.extend(list(MONTHS_DAYS))
    if request.GET.get('action') == 'remove_all_days':
        session.week_days = []
        session.months_days = []