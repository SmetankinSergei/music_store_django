from mail_service.forms import OneTimeMailForm, EventMailForm, WeekDayMailForm, MonthDayMailForm

FORMS_DICT = {
    'one_time': OneTimeMailForm,
    'event': EventMailForm,
    'week_day': WeekDayMailForm,
    'month_day': MonthDayMailForm,
}

MAILING_SERVICES = [
    {'name': 'one_time', 'description': 'One-time mailing to one or more recipients'},
    {'name': 'event', 'description': 'Mailing for some event, for example - purchase. To one or more recipients'},
    {'name': 'week_day', 'description': 'Newsletter on specific days of the week. To one or more recipients'},
    {'name': 'month_day', 'description': 'Newsletter on specific dates of the month. To one or more recipients'},
]
