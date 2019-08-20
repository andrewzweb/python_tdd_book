from django.shortcuts import render
from django.http import HttpResponse

# Создайте ваши представления здесь.
def home_page(request):
    '''домашняя страница'''
    template = '<html><title>To-Do lists</title></html>'
    return HttpResponse(template)

