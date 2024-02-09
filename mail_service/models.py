from django.db import models

NULLABLE = {'null': True, 'blank': True}


class BaseMailServiceAction(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class Mailing(models.Model):
    subject = models.CharField(max_length=250)
    content = models.TextField(**NULLABLE)
    # created_at = models.DateTimeField(auto_now_add=True)
    # mailing_type = models.CharField(max_length=100)
    # week_day = models.PositiveIntegerField(default=0)
    # month_day = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = 'Mailing'
        verbose_name_plural = 'Mailings'
