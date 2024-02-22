from django.views.generic import CreateView, UpdateView, DeleteView, DetailView, TemplateView

from mail_service.forms import MailingForm
from mail_service.models import MailContent, Recipient
from mail_service.session import session
from mail_service.templatetags.mail_service_tags import get_recipients_list


class MailServiceListView(TemplateView):
    template_name = 'mail_service_list.html'
    extra_context = {'title': 'mail service'}


class MailingDetailView(DetailView):
    pass


class MailingCreateView(CreateView):
    model = MailContent
    form_class = MailingForm
    template_name = 'mailing_form.html'
    session.clear_session()
    extra_context = {'session': session}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        service_name = self.kwargs.get('service_name')
        context['title'] = service_name.replace('_', ' ') + ' LETTER'
        session.mailing_type = service_name
        action = self.request.GET.get('action')
        new_letter = self.request.GET.get('new_letter')
        context['new_letter'] = new_letter

        if action == 'add':
            recipient_pk = self.request.GET.get('recipient_pk')
            recipient = Recipient.objects.get(pk=recipient_pk)
            session.recipients_list.append(recipient)
        elif action == 'remove':
            recipient_pk = self.request.GET.get('recipient_pk')
            recipient = Recipient.objects.get(pk=recipient_pk)
            session.recipients_list.remove(recipient)
        elif action == 'add_all':
            session.recipients_list = list(get_recipients_list())
        elif action == 'remove_all':
            session.recipients_list = []

        if self.request.GET.get('show_letter'):
            letter = MailContent.objects.get(pk=self.request.GET.get('show_letter'))
            session.show_letters_list.append(letter)

        if self.request.GET.get('hide_letter'):
            letter = MailContent.objects.get(pk=self.request.GET.get('hide_letter'))
            session.show_letters_list.remove(letter)

        if self.request.GET.get('add_letter'):
            session.letter = MailContent.objects.get(pk=self.request.GET.get('add_letter'))

        if self.request.GET.get('remove_letter'):
            session.letter = None

        if self.request.GET.get('month_day'):
            day = int(self.request.GET.get('month_day'))
            if day not in session.months_days:
                session.months_days.append(day)
            else:
                session.months_days.remove(day)

        if self.request.GET.get('week_day'):
            day = self.request.GET.get('week_day')
            if day not in session.week_days:
                session.week_days.append(day)
            else:
                session.week_days.remove(day)

        return context


class MailingUpdateView(UpdateView):
    pass


class MailingDeleteView(DeleteView):
    pass
