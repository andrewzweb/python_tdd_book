from django.core import mail
from selenium.webdriver.common.keys import Keys
import re 

from .base import FunctionalTest

TEST_EMAIL = 'luci@gmail.com'
SUBJECT = 'Your login link for Superlists'

class LoginTest(FunctionalTest):
    '''test login in system'''

    def test_redirects_to_home_page(self):
        '''test redirect to home page'''
        response = self.client.get('/accounts/login?token=abcd123')
        self.assertRedirects(response, '/')

    def test_can_get_email_link_to_log_in(self):
        '''test: can get email link to log in'''

        # Luci go to home
        # Site say Luci login 
        
        self.browser.get(self.live_server_url)
        self.browser.find_element_by_name('email').send_keys(TEST_EMAIL)
        self.browser.find_element_by_name('email').send_keys(Keys.ENTER)

        # show message send on mail letter

        self.wait_for(lambda: self.assertIn(
            'Check you message, we send You link, which can use login in site',
            self.browser.find_element_by_tag_name('body').text
        ))

        # Luci watch inbox 

        email = mail.outbox[0]
        self.assertIn(TEST_EMAIL, email.to)
        self.assertEqual(email.subject, SUBJECT)

        # Mail contant url
        self.assertIn('Use this link to log in', email.body)
        url_search = re.search(r'http://.+/.+$', email.body)
        if not url_search:
            self.fail(f'Counld not find url in email body:\n{email.body}')
        
        url = url_search.group(0)

        self.assertIn(self.live_server_url, url)
        
        # Luci press t botton
        self.browser.get(url)

        # She registry in system 
        self.wait_to_be_logged_in(email=TEST_EMAIL)

        # now she out 
        self.browser.find_element_by_link_text('Log Out').click()

        # now She logout 
        self.wait_to_be_logged_out(email=TEST_EMAIL)


        
