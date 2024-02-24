from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView, TemplateView

from mail_service.forms import MailingForm
from mail_service.models import MailContent, Mailing, Recipient
from mail_service.request_handler import recipient_handler, letter_handler, period_handler, time_handler
from mail_service.session import session


class MailServiceListView(TemplateView):
    template_name = 'mail_service_list.html'
    extra_context = {'title': 'mail service'}

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        session.clear_session()
        return context


class MailingDetailView(DetailView):
    model = Mailing

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title'] = 'mailing details'
        try:
            recipients = self.object.recipients.all()
        except AttributeError:
            recipients = []
        context['recipients'] = recipients
        return context


class MailingCreateView(CreateView):
    model = MailContent
    form_class = MailingForm
    template_name = 'mailing_form.html'
    session.clear_session()
    extra_context = {'session': session}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        service_name = self.kwargs.get('service_name')
        session.mailing_type = service_name
        context['title'] = service_name.replace('_', ' ') + ' LETTER'
        new_letter = self.request.GET.get('new_letter')
        context['new_letter'] = new_letter
        recipient_handler(self.request)
        letter_handler(self.request)
        period_handler(self.request)
        if self.request.GET.get('hours'):
            time_handler(self.request)
        return context


class MailingUpdateView(UpdateView):
    model = Mailing
    fields = ['letter']
    template_name = 'mailing_update_form.html'
    success_url = reverse_lazy('mail_service:mail_service')


class MailingDeleteView(DeleteView):
    model = Mailing
    success_url = reverse_lazy('mail_service:mail_service')
    extra_context = {'title': 'delete mailing'}

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['session'] = session
        return context


def confirm_mailing(request):
    mailing = Mailing.objects.create(
        send_time=session.mailing_time,
        letter=session.letter,
        mailing_type=session.mailing_type,
    )
    if session.week_days:
        mailing.week_days = ','.join(session.week_days)
    elif session.months_days:
        mailing.month_days = ','.join([str(i) for i in session.months_days])
    mailing.save()
    recipients_list = [Recipient.objects.get(full_name=recipient) for recipient in session.recipients_list]
    mailing.recipients.set(recipients_list)
    return redirect('mail_service:mail_service')
