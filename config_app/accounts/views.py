import sys
from django.contrib.auth import authenticate
from django.contrib import messages, auth
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from accounts.models import Token 
from django.core.urlresolvers import reverse

def send_login_email(request):
    '''send link on email'''
    email = request.POST['email']
    token = Token.objects.create(email=email)

    url = request.build_absolute_uri(
        reverse('login')+ '?token=' + str(token.uid)
    )

    message_body = f'Use this link to log in: \n\n{url}'

    send_mail(
        'Your login link for Superlists',
        message_body,
        'noreply@superlists',
        [email]
    )

    messages.success(
        request,
        'Check you message, we send You link, which can use login in site'
    )
    return redirect('/')


def login(request):
    print('login view', file=sys.stderr)
    uid = request.GET.get('uid')
    user = auth.authenticate('uid')
    if user is not None:
        auth.login(request, user)
    return redirect('/')
