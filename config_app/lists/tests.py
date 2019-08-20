from django.http import HttpRequest
from django.urls import resolve
from django.test import TestCase
from django.template.loader import render_to_string

from lists.views import home_page
from lists.models import Item

 
class HomePageTest(TestCase):
    '''тест домашней страницы'''

    def test_root_url_resolves_to_home_page_view(self):
        '''тест: корневой url преобразуется в представление
        домашней страницы'''
        found = resolve('/')
        self.assertEqual(found.func, home_page) 

    def test_home_page_returns_correct_html(self):
        '''тест: домашняя страница возвращает правильный html'''
        response = self.client.get('/') 
        self.assertTemplateUsed(response, 'home.html')

    def test_can_save_a_POST_request(self):
        """ тест: можно сохранить post-запрос """
        response = self.client.post('/', data={'item_text':'A new list item'})
        
        self.assertEqual(Item.objects.count(),1)
        new_item = Item.objects.first()
        self.assertEqual(new_item.text, 'A new list item')

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'], '/')


    def test_only_saves_items_when_necessary(self):
        '''тест: сохраняет элементы, только когда нужно'''
        self.client.get('/')
        self.assertEqual(Item.objects.count(), 0)


class ItemModelTest(TestCase):
    '''tets models '''

    def test_saving_and_retrieving_items(self):
        '''test saving and get element of list'''
        first_item = Item()
        first_item.text = 'The first (ever) list item'
        first_item.save() 
        

        second_item = Item()
        second_item.text = 'Item the second'
        second_item.save()
        
        saved_items = Item.objects.all()
        self.assertEqual(saved_items.count(), 2)
        
        first_saved_item = saved_items[0].text
        second_saved_item = saved_items[1].text
        self.assertEqual(first_saved_item, 'The first (ever) list item')
        self.assertEqual(second_saved_item, 'Item the second')
