from django import forms

from mail_service.models import MailContent


class MailingForm(forms.ModelForm):
    class Meta:
        model = MailContent
        fields = ['subject', 'content']
