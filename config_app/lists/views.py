from django.shortcuts import redirect, render
from django.http import HttpResponse
from lists.models import Item, List


def home_page(request):
    '''home page'''
    return render(request, 'home.html')


def view_list(request):
    ''' view list '''
    items = Item.objects.all()
    return render(request, 'list.html', {'items': items})


def new_list(request):
    ''' view list '''
    list_ = List.objects.create()
    Item.objects.create(text=request.POST['item_text'], list=list_)
    return redirect('/lists/one-of-the-world/')

