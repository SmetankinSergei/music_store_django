from django.views.generic import CreateView, UpdateView, DeleteView, DetailView, TemplateView

from mail_service.forms import MailingForm
from mail_service.models import MailContent
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
    pass


class MailingDeleteView(DeleteView):
    pass
