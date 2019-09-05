from selenium.webdriver.common.keys import Keys
from .base import FunctionalTest

class ItemValidationTest(FunctionalTest):
    ''' test valid new element '''

    def get_error_element(self):
        '''get error'''
        return self.browser.find_element_by_css_selector('.has-error')

    def test_cannot_add_empty_list_items(self):
        '''test: can not use empty element  '''
        
        # Luci open home page and try send empmty item of list
        self.browser.get(self.live_server_url)
        inputbox = self.get_item_input_box().send_keys(Keys.ENTER)


        # home reload and show error messege 
        # what say element can not be empty
        
        self.wait_for(lambda: self.browser.find_element_by_css_selector('#id_text:invalid'))

        # now she try with text and its work 
        self.get_item_input_box().send_keys("Buy milk")
        self.get_item_input_box().send_keys(Keys.ENTER)


        # how not strange she deside send empty element
        self.get_item_input_box().send_keys(Keys.ENTER)
        
        # Luci get error in page 
        self.wait_for(lambda: self.browser.find_element_by_css_selector('#id_text:invalid'))
        
        self.get_item_input_box().send_keys("Make tea")
        self.get_item_input_box().send_keys(Keys.ENTER)

        self.wait_for_row_in_list_table('1: Buy milk')
        self.wait_for_row_in_list_table('2: Make tea')


    def test_cannot_add_dublicate_items(self):
        ''' test cannot add dublicate items'''

        # Luci open home page and try send empmty item of list
        self.browser.get(self.live_server_url)
        self.get_item_input_box().send_keys('Buy wellies')
        self.get_item_input_box().send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy wellies')

        # accidentally input the same 
        self.get_item_input_box().send_keys('Buy wellies')
        self.get_item_input_box().send_keys(Keys.ENTER)

        # home reload and show error messege 
        # what say element can not be dublicate
        self.wait_for(lambda: self.assertEqual(self.get_error_element().text,
                      "You've already got this in your list"
        ))

    def test_error_messages_are_cleared_on_input(self):
        '''test error messages are cleared on input'''

        # Luci start new list 
        self.browser.get(self.live_server_url)
        self.get_item_input_box().send_keys('Banter too thick')
        self.get_item_input_box().send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Banter too thick')

        # accidentally input the same 
        self.get_item_input_box().send_keys('Banter too thick')
        self.get_item_input_box().send_keys(Keys.ENTER)

        self.wait_for(lambda: self.assertTrue(
            self.get_error_element().is_displayed()
        ))

        # she start write and error hide 
        self.get_item_input_box().send_keys('a')
        self.get_item_input_box().send_keys(Keys.ENTER)

        self.wait_for(lambda: self.assertFalse(
            self.get_error_element().is_displayed()
        ))
        

        
