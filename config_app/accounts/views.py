import uuid
import sys 
from django.shortcuts import render
from django.core.mail import send_mail

from accounts.models import Token 


def send_login_email(request):
    '''send link on email'''

    email = request.POST['email']
    uid = str(uuid.uuid4())
    Token.objects.create(email=email, uid=uid)
    
    print('saving uid', uid, 'for mail', email, file=sys.stderr)
    send_mail(
        'You login link for Lists',
        f'Use this link to log in:\n\n{url}',
        'email_my_app@mail'
        [email]
    )
    
    return render(request, 'login_email_sent.html')
