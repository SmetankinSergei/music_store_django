MAILING_SERVICES = [
    {'name': 'one_time', 'description': 'One-time mailing to one or more recipients'},
    {'name': 'event', 'description': 'Mailing for some event, for example - purchase. To one or more recipients'},
    {'name': 'week_day', 'description': 'Newsletter on specific days of the week. To one or more recipients'},
    {'name': 'month_day', 'description': 'Newsletter on specific dates of the month. To one or more recipients'},
]

MAILING_TYPES = [
    ('ONE_TIME', 'one_time'),
    ('EVERY_WEEK', 'every_week'),
    ('EVERY_MONTH', 'every_month'),
]

MAILING_STATUSES = [
    ('CREATED', 'created'),
    ('IN_PROGRES', 'in_progres'),
    ('SENT', 'sent'),
]

FAKE_RECIPIENTS_AMOUNT = 20
