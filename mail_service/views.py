from django.views.generic import CreateView, UpdateView, DeleteView, DetailView, TemplateView

from mail_service.constants import FORMS_DICT
from mail_service.models import Mailing


class MailServiceListView(TemplateView):
    template_name = 'mail_service_list.html'
    extra_context = {'title': 'mail service'}


class MailingDetailView(DetailView):
    pass


class MailingCreateView(CreateView):
    model = Mailing
    template_name = 'mailing_form.html'
    extra_context = {'title': 'new mailing'}

    def get_form_class(self):
        form_name = self.kwargs['form_name']
        return FORMS_DICT[form_name]


class MailingUpdateView(UpdateView):
    pass


class MailingDeleteView(DeleteView):
    pass
