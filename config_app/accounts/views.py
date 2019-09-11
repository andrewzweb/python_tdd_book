import uuid
import sys 
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.shortcuts import render, redirect
from django.core.mail import send_mail

from accounts.models import Token 


def send_mail(request):
    '''send link on email'''
    email = request.POST['email']
    send_mail(
        'Your login link for Superlists',
        'body text tbc',
        'noreply@superlists',
        [email])
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
