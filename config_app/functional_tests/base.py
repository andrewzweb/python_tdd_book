import os
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver 
import time 

MAX_WAIT = 10

class FunctionalTest(StaticLiveServerTestCase):
    """ test new user """

    def setUp(self):
        self.browser = webdriver.Firefox()
        staging_server = os.environ.get('STAGING_SERVER')
        if staging_server: 
            self.live_server_url = 'http://' + staging_server

    def tearDown(self):
        self.browser.quit()


    def test_can_a_list_and_retrieve_it_later(self):
        """ test : can start and get list """
        self.browser.get(self.live_server_url)
        self.assertIn('To-Do', self.browser.title)

    def wait_for_row_in_list_table(self, row_text):
        ''' wait str in table '''

        start_time = time.time()
        while True:
            try: 
                table = self.browser.find_element_by_id('id_list_table')
                rows = table.find_elements_by_tag_name('tr')
                self.assertIn(row_text, [row.text for row in rows])
                return
            except (AssertionError, WebDriverException) as e:
                if time.time() - start_time > MAX_WAIT:
                    raise e
                time.sleep(0.5)

    def wait_for(self, fn):
        ''' wait str in table '''

        start_time = time.time()
        while True:
            try: 
                return fn()
            except (AssertionError, WebDriverException) as e:
                if time.time() - start_time > MAX_WAIT:
                    raise e
                time.sleep(0.5)

