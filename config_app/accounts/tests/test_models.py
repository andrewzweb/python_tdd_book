from django.test import TestCase
from django.contrib.auth import get_user_model
from django.contrib import auth
from accounts.models import Token

User = get_user_model()

class UserModelTest(TestCase):
    '''test user model'''

    def test_user_is_valid_with_email_only(self):
        '''test: user valid only with mail '''

        user = User(email='a@b.com')
        user.full_clean() # don't sent error

    def test_email_is_primary_key(self):
        '''test: adress email in primary key '''
        user = User(email='a@b.com')
        self.assertEqual(user.pk, 'a@b.com')

    def test_links_user_with_auto_genereted_uid(self):
        '''test connect user with uid'''

        token1 = Token.objects.create(email='a@b.com')
        token2 = Token.objects.create(email='a@b.com')
        self.assertNotEqual(token1.uid, token2.uid)

    def test_no_problem_with_auth_login(self):
        '''test problem with auth no '''
    
        user = User.objects.create(email='luci@gmail.com')
        user.backend = ''
        request = self.client.request().wsgi_request
        auth.login(request, user)

