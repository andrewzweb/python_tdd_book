from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
import time
import unittest 


class NewVisitorTest(unittest.TestCase):
    """ test new user """


    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()


    def test_can_a_list_and_retrieve_it_later(self):
        """ test : can start and get list """
        self.browser.get("http://localhost:8000")
        self.assertIn('To-Do', self.browser.title)
        self.fail('End test!')

        def check_for_row_in_list_table(self, row_text):
            '''подтверждение строки в таблице списка'''
            table = self.browser.find_element_by_id('id_list_table')
            rows = table.find_elements_by_tag_name('tr')
            self.assertIn(row_text, [row.text for row in rows])


    def test_can_start_a_list_and_retrieve_it_later(self):
        '''test: can start list and get him later'''
        # Lusi hear about new app with lists
        # and want see this app 
        self.browser.get('http://localhost:8000')
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
        inputbox.send_keys('1: Buy somthing') 
        # When she press enter, page  updated
        # now page consist  "Buy something"

        inputbox.send_keys(Keys.ENTER) 
        time.sleep(3) 
        self.check_for_row_in_list_table("1: Buy somthing")


        # Text field invites she add element 
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('2: Make')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        self.check_for_row_in_list_table("1: Buy somthing")
        self.check_for_row_in_list_table("2: Make")

        self.fail('Test fail!')

if __name__ == "__main__":
    unittest.main(warnings='ignore')

