from django.test import TestCase
from unittest.mock import patch 

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

