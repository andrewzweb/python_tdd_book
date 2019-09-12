from django.test import TestCase
from unittest.mock import patch, call

class SendLoginEmailViewTest(TestCase):
    '''test view with send email for login in sys'''


    @patch('accounts.views.send_mail')
    def test_send_mail_to_address_from_post(self, mock_send_mail):
        '''test send email'''

        self.client.post('/accounts/send_login_email', data={'email':'luci@example.com'})
        
        self.assertTrue(mock_send_mail.called, True)
        (subject, body, from_email, to_list), kwargs = mock_send_mail.call_args
        self.assertEqual(subject, 'Your login link for Superlists')
        self.assertEqual(from_email, 'noreply@superlists')
        self.assertEqual(to_list, ['luci@example.com'])

    def test_adds_success_message(self):
        '''test add masega about success'''

        response = self.client.post('/accounts/send_login_email', 
            data = {'email': 'luci@example.com'}, follow=True
        )

        message = list(response.context['messages'])[0]
        
        self.assertEqual(
            message.message, 
            'Check you message, we send You link, which can use login in site'
        )
        self.assertEqual(message.tags, 'success')

    @patch('accounts.views.messages')
    def test_adds_success_message_with_mocks(self, mock_messages):
        '''test send messages'''

        response = self.client.post(
            '/accounts/send_login_email', 
            data={'email':'luci@example.com'}
        )
        
        expected = 'Check you message, we send You link, which can use login in site'
        
        self.assertEqual(
            mock_messages.success.call_args, 
            call(response.wsgi_request, expected)
        )





