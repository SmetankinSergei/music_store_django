from django.views.generic import CreateView, UpdateView, DeleteView, DetailView, TemplateView

from mail_service.forms import MailingForm
from mail_service.models import Mailing, MailContent, Recipient
from mail_service.session import Session, session
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
    extra_context = {'title': 'new mailing', 'session': session}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        service_name = self.kwargs.get('service_name')
        context['service_name'] = service_name
        action = self.request.GET.get('action')
        if action == 'add':
            recipient_pk = self.request.GET.get('recipient_pk')
            recipient = Recipient.objects.get(pk=recipient_pk)
            session.recipients_list.append(recipient)
        elif action == 'remove':
            recipient_pk = self.request.GET.get('recipient_pk')
            recipient = Recipient.objects.get(pk=recipient_pk)
            session.recipients_list.remove(recipient)
        elif action == 'add_all':
            session.recipients_list = get_recipients_list()
        elif action == 'remove_all':
            session.recipients_list = []
        return context


class MailingUpdateView(UpdateView):
    pass


class MailingDeleteView(DeleteView):
    pass
