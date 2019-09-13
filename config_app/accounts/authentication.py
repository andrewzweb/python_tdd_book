import sys 
from accounts.models import User, Token


class PasswordlessAuthenticationBackend(object):
    '''server process no password auth'''

    def authenticate(self, uid):
        '''auth'''
        try:
            token = Token.objects.get(uid=uid)
            return User.objects.get(email=token.email)
        
        except User.DoesNotExist:
            return User.objects.create(email=token.email)
        except Token.DoesNotExist:
            return None

    def get_user(self, email):
        '''get user'''
        try:
            User.objects.get(email=email)
        except:
            return None

