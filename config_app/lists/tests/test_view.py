from django.http import HttpRequest
from django.urls import resolve
from django.test import TestCase
from django.template.loader import render_to_string
from django.utils.html import escape

from lists.views import home_page
from lists.models import Item, List

 
class HomePageTest(TestCase):
    '''тест домашней страницы'''

    def test_root_url_resolves_to_home_page_view(self):
        '''тест: корневой url преобразуется в представление
        домашней страницы'''
        found = resolve('/')
        self.assertEqual(found.func, home_page) 

    def test_only_saves_items_when_necessary(self):
        '''тест: сохраняет элементы, только когда нужно'''
        self.client.get('/')
        self.assertEqual(Item.objects.count(), 0)


class ListViewTest(TestCase):
    
    def test_uses_list_template(self):
        ''' test: use template of the list  '''
        list_ = List.objects.create()
        response = self.client.get(f'/lists/{list_.id}/')
        self.assertTemplateUsed(response, 'list.html')

    def test_passes_correct_list_to_template(self):
        '''test get correct template'''

        other_list = List.objects.create()
        correct_list = List.objects.create()
        
        response = self.client.get(f'/lists/{correct_list.id}/')
        self.assertEqual(response.context['list'], correct_list)


    def test_displays_only_items_for_that_list(self):
        ''' test: show only items of this list '''
        correct_list = List.objects.create()
        
        Item.objects.create(text='item 1', list=correct_list)
        Item.objects.create(text='item 2', list=correct_list)

        other_list = List.objects.create()
        Item.objects.create(text='other item 1', list=other_list)
        Item.objects.create(text='other item 2', list=other_list)

        response = self.client.get(f'/lists/{correct_list.id}/')
        
        self.assertContains(response, 'item 1')
        self.assertContains(response, 'item 2')
        self.assertNotContains(response, 'other item 1')
        self.assertNotContains(response, 'other item 2')

    def test_can_save_a_POST_request_to_an_existing_list(self):
        '''test can save a POST request to an existing list'''
        other_list = List.objects.create()
        correct_list = List.objects.create()
        self.client.post(
            f'/lists/{correct_list.id}/',
            data = {'item_text': 'A new item foe an existing list'}
        )

        self.assertEqual(Item.objects.count(), 1)
        new_item = Item.objects.first()
        self.assertEqual(new_item.text, 'A new item foe an existing list')
        self.assertEqual(new_item.list, correct_list)


    def test_POST_redirect_to_list_view(self):
        ''' test post redirect in list view '''
        other_list = List.objects.create()
        correct_list = List.objects.create()
        
        response = self.client.post(
            f'/lists/{correct_list.id}/',
            data = {'item_text': 'A new item foe an existing list'}
        )
        
        self.assertRedirects(response, f'/lists/{correct_list.id}/')

 
class NewListTest(TestCase):
    '''test new list '''

    def test_can_save_a_POST_request(self):
        '''test: can save after POST'''
        self.client.post('/lists/new', data={'item_text': 'A new list item'})
        self.assertEqual(Item.objects.count(), 1)
        new_item = Item.objects.first()
        self.assertEqual(new_item.text, 'A new list item')

    def test_redirects_after_POST(self):
        '''test: redirect adter POST'''
        response = self.client.post('/lists/new', data={'item_text': 'A new list item'})
        new_list = List.objects.first()
        self.assertRedirects(response, f'/lists/{new_list.id}/')

    def test_validation_errors_are_sent_back_to_home_page_template(self):
        '''test error validation get back in template'''
        response = self.client.post('/lists/new', data={'item_text': ''})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')
        expected_error = escape("You can't have an empty list item")
        self.assertContains(response, expected_error)
        

    def test_invalid_list_items_arent_saved(self):
        '''test don't save invalid items'''
        response = self.client.post('/lists/new', data={'item_text': ''})
        self.assertEqual(List.objects.count(), 0)
        self.assertEqual(Item.objects.count(), 0)

        

class NewItemTest(TestCase):
    '''test new list item'''


    def test_can_save_a_POST_request_to_an_existing_list(self):
        '''test can save in post-request in existing list'''
        other_list = List.objects.create()
        correct_list = List.objects.create()
        
        self.client.post(
            f'/lists/{correct_list.id}/',
            data={'item_text':'A new item for an existing list'}
        )

        #self.assertEqual(Item.objects.count(), 1)
        new_item = Item.objects.first()
        self.assertEqual(new_item.text, 'A new item for an existing list')
        self.assertEqual(new_item.list, correct_list)

    def test_redirects_to_list_view(self):
        '''test redirect after POST'''

        other_list = List.objects.create()
        correct_list = List.objects.create()
        
        response = self.client.post(
            f'/lists/{correct_list.id}/',
            data={'item_text':'A new item for an existing list'}
        )
        
        self.assertRedirects(response, f'/lists/{correct_list.id}/')
        


