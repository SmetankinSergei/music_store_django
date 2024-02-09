from django import forms

from mail_service.models import Mailing


class OneTimeMailForm(forms.ModelForm):
    class Meta:
        model = Mailing
        fields = ['subject']


class EventMailForm(forms.ModelForm):
    class Meta:
        model = Mailing
        fields = ['subject']


class WeekDayMailForm(forms.ModelForm):
    class Meta:
        model = Mailing
        fields = ['subject']


class MonthDayMailForm(forms.ModelForm):
    class Meta:
        model = Mailing
        fields = ['subject']
