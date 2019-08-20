from django.http import HttpRequest
from django.urls import resolve
from django.test import TestCase
from django.template.loader import render_to_string


from lists.views import home_page
 
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



