MAILING_SERVICES = [
    {'name': 'ONE_TIME', 'description': 'One-time mailing to one or more recipients'},
    {'name': 'WEEK_DAY', 'description': 'Newsletter on specific days of the week. To one or more recipients'},
    {'name': 'MONTH_DAY', 'description': 'Newsletter on specific dates of the month. To one or more recipients'},
]

MAILING_TYPES = [
    ('ONE_TIME', 'ONE_TIME'),
    ('WEEK_DAY', 'WEEK_DAY'),
    ('MONTH_DAY', 'MONTH_DAY'),
]

MAILING_STATUSES = [
    ('CREATED', 'CREATED'),
    ('IN_PROGRES', 'IN_PROGRES'),
    ('SENT', 'SENT'),
]

FAKE_RECIPIENTS_AMOUNT = 20

WEEK_DAYS = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
MONTHS_DAYS = range(1, 32)
SHORT_MONTHS = [4, 6, 9, 11]
