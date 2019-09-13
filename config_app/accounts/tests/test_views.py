from django.test import TestCase
from unittest.mock import patch, call
from accounts.models import Token 
from accounts.views import send_login_email



class SendLoginEmailViewTest(TestCase):
    '''test view with send email for login in sys'''


    def post_send_email(self):
        response = self.client.post(
            f'/accounts/send_login_email', 
            data={'email':'luci@gmail.com'})
        return response 

    def test_redirect_to_home_page(self):
        '''test redirect'''
        response = self.post_send_email()
        self.assertRedirects(response, '/')


    def test_adds_success_message(self):
        '''test add masega about success'''

        response = self.client.post('/accounts/send_login_email', 
            data = {'email': 'luci@gmail.com'}, follow=True
        )
        message = list(response.context['messages'])[0]
        self.assertEqual(
            message.message, 
            'Check you message, we send You link, which can use login in site'
        )
        self.assertEqual(message.tags, 'success')


    @patch('accounts.views.send_mail')
    def test_send_mail_to_address_from_post(self, mock_send_mail):
        '''test send email'''

        response = self.post_send_email()
        
        self.assertTrue(mock_send_mail.called, True)
        (subject, body, from_email, to_list), kwargs = mock_send_mail.call_args
        self.assertEqual(subject, 'Your login link for Superlists')
        self.assertEqual(from_email, 'noreply@superlists')
        self.assertEqual(to_list, ['luci@gmail.com'])


    @patch('accounts.views.messages')
    def test_adds_success_message_with_mocks(self, mock_messages):
        '''test send messages'''
        response = self.post_send_email()
        expected = 'Check you message, we send You link, which can use login in site'
        self.assertEqual(
            mock_messages.success.call_args, 
            call(response.wsgi_request, expected)
        )

    def test_creates_token_associated_with_email(self):
        '''test: create marker associated with email'''
        self.post_send_email()
        token = Token.objects.first()
        self.assertEqual(token.email, 'luci@gmail.com')


    @patch('accounts.views.auth')
    def test_sends_link_to_login_using_token_uid(self, mock_auth):
        '''test sends link to login using token uid'''
        response = self.client.get('/accounts/login?token=abcd123')
        self.assertEqual(
            mock_auth.login.call_args,
            call(response.wsgi_request, mock_auth.authenticate.return_value)
        )

@patch('accounts.views.auth')
class LoginViewTest(TestCase):
    '''test view'''

    def test_redirect_to_home_page(self, mock_auth):
        '''test redirect to home page'''
        pass

    def test_calls_authenticate_with_uid_from_get_request(self, mock_auth):
        '''test calls authenticate with uid from get request'''
        pass

    def test_calls_auth_ligin_with_user_if_there_is_one(self, mock_auth):
        '''test calls auth ligin with user if there is one'''
        pass

    def test_does_calls_auth_login_with_user_if_there_is_one(self, mock_auth):
        '''test does calls auth login with user if there is one'''
        mock_auth.authenticate.return_value = None
        response = self.client.get('/accounts/login?token=abcd123')
        self.assertEqual(mock_auth.login.called, False)
        
