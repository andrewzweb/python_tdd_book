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


    def test_can_start_a_list_for_one_user(self):
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
        inputbox.send_keys('buy peacock feathers') 
        # When she press enter, page  updated
        # now page consist  "Buy something"

        inputbox.send_keys(Keys.ENTER) 
        self.wait_for_row_in_list_table("1: buy peacock feathers")


        # Text field invites she add element 
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys("make a fly")
        inputbox.send_keys(Keys.ENTER)

        self.wait_for_row_in_list_table("1: buy peacock feathers")
        self.wait_for_row_in_list_table("2: make a fly")
        

    def test_multiple_users_can_start_lists_at_different_urls(self):
        ''' test: multiple users can start lists at different urls'''
        
        # Lusi star tnew list
        self.browser.get(self.live_server_url)
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('buy peacock feathers')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: buy peacock feathers')
        # She see list have uniq url
        edith_list_url = self.browser.current_url
        self.assertRegex(edith_list_url, '/lists/.+') 

        # Now user Feliks go to site 
        ## use new seccion becouse we need insulation
        ## info Lisi dont gone for cookie
        self.browser.quit()
        self.browser = webdriver.Firefox()
        # Feliks see home page no mark Lusi
        self.browser.get(self.live_server_url)
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('buy peacock feathers', page_text)
        self.assertNotIn('make a fly', page_text)
        # Feliks start new list 
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Buy milk')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy milk')
        # Feliks get uniq url 
        francis_list_url = self.browser.current_url
        self.assertRegex(francis_list_url, '/lists/.+')
        self.assertNotEqual(francis_list_url, edith_list_url)
        # Again not mark Lusi
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('buy peacock feathers', page_text)
        self.assertIn('Buy milk', page_text)

        # satisfied go to bed
