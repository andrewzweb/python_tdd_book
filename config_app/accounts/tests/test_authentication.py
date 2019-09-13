from django.test import TestCase
from django.contrib.auth import get_user_model
from accounts.authentication import PasswordlessAuthenticationBackend
from accounts.models import Token

User = get_user_model()

class AuthenticateTest(TestCase):
    '''test authenticate'''


    def test_returns_None_if_no_shuch_token(self):
        '''test: return if user don't exist '''
        result = PasswordlessAuthenticationBackend().authenticate('no-such-token')
        self.assertIsNone(result)


    def test_returns_new_user_with_correct_email_if_token_exists(self):
        '''test returns new user with correct email if token exists'''
        email = 'luci@gmail.com'
        token = Token.objects.create(email=email)
        user = PasswordlessAuthenticationBackend().authenticate(token.uid)
        new_user = User.objects.get(email=email)

        self.assertEqual(user, new_user)


class GetUserTest(TestCase):
    '''tests get user '''

    
    def test_gets_user_by_email(self):
        '''test get user by email'''

        User.objects.create(email='test@user.com')
        desired_user = User.objects.create(email='luci@gmail.com')
        found_user = PasswordlessAuthenticationBackend().get_user(
            'luci@gmail.com'
        )
        
    def test_returns_None_if_no_user_with_that_email(self):
        ''''test: returns None if no user with that email'''

        self.assertIsNone(
            PasswordlessAuthenticationBackend().get_user('luci@gmail.com')
        )

     
