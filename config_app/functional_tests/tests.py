from django.test import LiveServerTestCase
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException
import time
import unittest 

MAX_WAIT = 10

class NewVisitorTest(LiveServerTestCase):
    """ test new user """

    def setUp(self):
        self.browser = webdriver.Firefox()

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


    def test_can_start_a_list_and_retrieve_it_later(self):
        '''test: can start list and get him later'''
        # Lusi hear about new app with lists
        # and want see this app 
        self.browser.get(self.live_server_url)
        # She see header and title tell about lists 
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)
        # She input element of list k
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )
        # They write in textfield "Buy something"
        inputbox.send_keys('Buy something') 
        # When she press enter, page  updated
        # now page consist  "Buy something"

        inputbox.send_keys(Keys.ENTER) 
        self.wait_for_row_in_list_table("1: Buy something")


        # Text field invites she add element 
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys("Make")
        inputbox.send_keys(Keys.ENTER)

        self.wait_for_row_in_list_table("1: Buy something")
        self.wait_for_row_in_list_table("2: Make")
        



