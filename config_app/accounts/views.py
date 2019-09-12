import uuid
import sys 
from django.contrib.auth import authenticate
from django.contrib import messages
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.shortcuts import render, redirect
from django.core.mail import send_mail

from accounts.models import Token 


def send_login_email(request):
    '''send link on email'''
    email = request.POST['email']
    recipient_list = [email]

    send_mail(
        'Your login link for Superlists',
        'body text tbc',
        'noreply@superlists',
        [email]
    )

    messages.add_message(
        request,
        messages.SUCCESS,
        'Check you message, we send You link, which can use login in site'
    )
    return redirect('/')


def login(self):
    '''registry in system'''

    print('login view', file=sys.stderr)
    uid = request.GET.get('uid')
    user = authenticate(uid=uid)
    if user is not None :
        auth_login(request, user)
    return redirect('/')

def logout(request):
    '''log out'''
    auth_logout(request)
    return redirect('/')

