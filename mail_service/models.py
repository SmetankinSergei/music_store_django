from django.urls import reverse
from django.utils import timezone

from django.db import models

from mail_service.constants import MAILING_TYPES, MAILING_STATUSES
from mail_service.session import session

NULLABLE = {'null': True, 'blank': True}


class Recipient(models.Model):
    email = models.EmailField()
    full_name = models.CharField(max_length=250)
    comment = models.TextField()

    class Meta:
        verbose_name = 'ServiceClient'
        verbose_name_plural = 'ServiceClients'


class Mailing(models.Model):
    send_time = models.TimeField(default=timezone.now)
    recipients = models.ManyToManyField(Recipient, related_name='recipients', **NULLABLE)
    mailing_type = models.CharField(max_length=50, choices=MAILING_TYPES, default=MAILING_TYPES[0][0])
    status = models.CharField(max_length=50, choices=MAILING_STATUSES, default=MAILING_STATUSES[0][0])

    class Meta:
        verbose_name = 'Mailing'
        verbose_name_plural = 'Mailings'


class MailContent(models.Model):
    subject = models.CharField(max_length=250)
    content = models.TextField()

    @staticmethod
    def get_absolute_url():
        return reverse('mail_service:new_mailing', kwargs={'service_name': session.mailing_type})

    class Meta:
        verbose_name = 'Letter'
        verbose_name_plural = 'Letters'


class MailLog(models.Model):
    last_attempt = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=50)
    service_answer = models.TextField()

    class Meta:
        verbose_name = 'MailLog'
        verbose_name_plural = 'MailLogs'
