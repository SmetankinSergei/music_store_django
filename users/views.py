from django.conf import settings
from django.contrib.auth import logout
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from users.constants import REGISTER_MAIL_MESSAGE
from users.forms import RegisterUserForm


def register(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()

            send_mail(
                subject='registration',
                message=REGISTER_MAIL_MESSAGE,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[user.email],
            )

            return render(request, 'users/register_done.html')
    else:
        form = RegisterUserForm()
    return render(request, 'users/register.html', {'form': form})


# class RegisterView(CreateView):
#     model = User
#     form_class = RegisterUserForm
#     template_name = 'users/register.html'
#     success_url = reverse_lazy('users:login')
#
#     def form_valid(self, form):
#         self.object = form.save()
#
#         return super().form_valid(form)


def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('users:login'))
