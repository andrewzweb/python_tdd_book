from django.test import TestCase
import accounts.views as account_views


class SendLoginEmailViewTest(TestCase):
    '''test view with send email for login in sys'''

    def test_send_mail_to_address_from_post(self):
        '''test send email'''

        self.send_mail_called = False


        def fake_send_mail(subject, body, from_email, to_list):
            '''fake send mail'''
            self.send_mail_called = True
            self.subject = subject
            self.body = body
            self.from_email = from_email
            self.to_list = to_list

        account_views.send_mail = fake_send_mail

        self.client.post('/accounts/send_login_email', data={'email':'luci@example.com'})
        
        self.assertTrue(self.send_mail_called)
        self.assertEqual(self.subject, 'Your login link for Superlists')
        self.assertEqual(self.from_email, 'noreply@superlists')
        self.assertEqual(self.to_list, ['luci@example.com'])

