from selenium.webdriver.common.keys import Keys
from .base import FunctionalTest

class ItemValidatorTest(FunctionalTest):
    ''' test valid new element '''


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

