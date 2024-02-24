from datetime import datetime, time

from django.core.mail import send_mail, BadHeaderError
from django.db.models import Q

from config.celery import app
from mail_service.constants import WEEK_DAYS_DICT, MAILING_STATUSES
from mail_service.models import Mailing, MailLog


@app.task(bind=True, ignore_result=True)
def mail_process(*args, **kwargs):
    current_datetime = datetime.now()
    current_date = current_datetime.date()
    current_day_number = current_date.day
    current_weekday = WEEK_DAYS_DICT[current_date.weekday()]
    current_time = current_datetime.time()
    current_day = {
        'MONTH_DAY': current_day_number,
        'WEEK_DAY': current_weekday
    }

    one_time_mailings = Mailing.objects.filter(
        Q(send_time__lte=current_time),
        Q(status__in=('CREATED', 'IN_PROGRES')),
        Q(mailing_type='ONE_TIME')
    )

    if time(16, 15) <= current_time <= time(16, 19):
        many_time_mailings = Mailing.objects.filter(
            Q(send_time__lte=current_time),
            Q(status__in=('CREATED', 'IN_PROGRES')),
            Q(mailing_type__in=('WEEK_DAY', 'MONTH_DAY'))
        )
        combined_mailings = many_time_mailings | one_time_mailings
    else:
        combined_mailings = one_time_mailings

    for mailing in combined_mailings:
        mailing.status = MAILING_STATUSES[1][0]
        mailing.save()
        if mailing.mailing_type == 'ONE_TIME':
            send_letters(mailing)
        else:
            if mailing.mailing_type == 'WEEK_DAY':
                days = mailing.week_days.split(',')
            else:
                days = [int(day) for day in mailing.month_days.split(',')]
            if current_day[mailing.mailing_type] in days:
                send_letters(mailing)


def send_letters(mailing):
    recipients_list = mailing.recipients.all()
    try:
        send_mail(
            mailing.letter.subject,
            mailing.letter.content,
            mailing.owner,
            recipients_list,
        )
        check_mailing_status(mailing)
        MailLog.objects.create(status=200, service_answer='OK')
    except BadHeaderError as err:
        MailLog.objects.create(status=500, service_answer=str(err))
    except ValueError as err:
        MailLog.objects.create(status=400, service_answer=str(err))


def check_mailing_status(mailing):
    current_date = datetime.now().date()
    if mailing.mailing_type == 'ONE_TIME' or current_date >= mailing.finish:
        mailing.status = MAILING_STATUSES[2][0]
        mailing.save()
