from django.conf import settings
from django.contrib.auth import BACKEND_SESSION_KEY, SESSION_KEY, get_user_model
from django.contrib.sessions.backends.db import SessionStore
from .base import FunctionalTest

User = get_user_model()

class MyListsTest(FunctionalTest):
    '''test app lists '''
    
    def create_pre_authenticated_sesssion(self, email):
        '''create pre authenticated sesssion'''
        user = User.objects.create(email=email)
        session = SessionStore()
        session[SESSION_KEY] = user.pk
        session[BACKEND_SESSION_KEY] = settings.AUTHENTICATION_BACKENDS[0]
        session.save()
        ## set cookie what need for first look domain
        ## page 404 get vary fast 
        self.browser.get(self.live_server_url + '/404_no_such_url/')
        self.browser.add_cookie(dict(
            name = settings.SESSION_COOKIE_NAME,
            value = session.session_key,
            path='/',
        ))
        

    
    def test_logged_in_users_lists_are_saved_as_my_lists(self):
        '''test lists register users'''
        
        email = 'luci@gmail.com'
        self.create_pre_authenticated_sesssion(email)

        # Luci open home page 
        self.browser.get(self.live_server_url)
        self.add_list_item('Reticulate splines')
        self.add_list_item('Immanentize eschaton')

        first_list_url = self.browser.current_url

        # she see lick on MyLists in first time

        self.browser.find_element_by_link_text('My lists').click()
        
        # she see, she was see her lists there and she named base on first element 
        self.wait_for(
            lambda: self.browser.find_element_by_link_text('Reticulate splines')
        )

        self.browser.find_element_by_link_text('Reticulate splines').click()
        
        self.wait_for(
            lambda: self.assertEqual(self.browser.current_url, first_list_url)
        )

        # she mind start new list 
        self.browser.get(self.live_server_url)
        self.add_list_item('Click cows')
        second_list_url = self.browser.current_url
        
        # in tabs MyLists see new list 
        self.browser.find_element_by_link_text("My lists").click()
        self.wait_for(
            lambda: self.browser.find_element_by_link_text('Click cows')
        )

        self.browser.find_element_by_link_text('Click cows').click()
        self.wait_for(
            lambda: self.assertEqual(self.browser.current_url, second_list_url)
        )
        
        # she logout and option MyList is not in display 
        self.browser.find_element_by_link_text('Log out').click()
        self.wait_for(
            lambda: self.assertEqual(
                self.browser.find_element_by_link_text('My lists'),
                []
            ))
        
