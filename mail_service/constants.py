MAILING_SERVICES = [
    {'name': 'ONE_TIME', 'description': 'One-time mailing to one or more recipients'},
    {'name': 'EVERY_WEEK', 'description': 'Newsletter on specific days of the week. To one or more recipients'},
    {'name': 'EVERY_MONTH', 'description': 'Newsletter on specific dates of the month. To one or more recipients'},
]

MAILING_TYPES = [
    ('ONE_TIME', 'ONE_TIME'),
    ('EVERY_WEEK', 'EVERY_WEEK'),
    ('EVERY_MONTH', 'EVERY_MONTH'),
]

MAILING_STATUSES = [
    ('CREATED', 'CREATED'),
    ('IN_PROGRES', 'IN_PROGRES'),
    ('SENT', 'SENT'),
]

FAKE_RECIPIENTS_AMOUNT = 20
