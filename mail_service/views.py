from django.views.generic import CreateView, UpdateView, DeleteView, DetailView, TemplateView

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


class MailingUpdateView(UpdateView):
    pass


class MailingDeleteView(DeleteView):
    pass
