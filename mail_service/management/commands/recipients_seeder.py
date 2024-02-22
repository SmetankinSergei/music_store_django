from django.core.management import BaseCommand

from mail_service.constants import FAKE_RECIPIENTS_AMOUNT
from mail_service.seeder import seed_recipients


class Command(BaseCommand):
    def handle(self, *args, **options):
        seed_recipients(FAKE_RECIPIENTS_AMOUNT)
