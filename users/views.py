from random import choice
from string import ascii_lowercase

from django.conf import settings
from django.contrib.auth import logout
from django.core.mail import EmailMultiAlternatives
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template.loader import render_to_string
from django.urls import reverse
from django.utils.html import strip_tags

from users.forms import RegisterUserForm
from users.models import User


def register(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            verification_token = generate_token()
            user.verification_token = verification_token
            user.is_active = False
            user.save()

            # send_mail(
            #     subject='registration',
            #     message=REGISTER_MAIL_MESSAGE + '&' + 'users/email_verification/' + verification_token,
            #     from_email=settings.EMAIL_HOST_USER,
            #     recipient_list=[user.email],
            # )

            verification_link = "http://127.0.0.1:8000/users/email_verification/?token={}&user_id={}"\
                .format(verification_token, user.pk)

            html_message = render_to_string('users/registration_email.html', {'verification_link': verification_link})
            text_message = strip_tags(html_message)

            msg = EmailMultiAlternatives(
                subject='Registration',
                body=text_message,
                from_email=settings.EMAIL_HOST_USER,
                to=[user.email],
            )
            msg.attach_alternative(html_message, "text/html")
            msg.send()

            return render(request, 'users/register_done.html')
    else:
        form = RegisterUserForm()
    return render(request, 'users/register.html', {'form': form})


def generate_token():
    token = ''
    for i in range(15):
        token += choice(ascii_lowercase)
    return token


def email_verification(request):
    if request.GET.get('token'):
        user = User.objects.get(pk=int(request.GET.get('amp;user_id')))
        user.is_active = True
        user.is_verify = True
        user.save()
    return render(request, 'users/verification_done.html')


def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('users:login'))
