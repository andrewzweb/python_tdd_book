from django.shortcuts import redirect, render
from django.http import HttpResponse
from lists.forms import ItemForm 
from lists.models import Item, List
from django.core.exceptions import ValidationError


def home_page(request):
    '''home page'''
    return render(request, 'home.html', {'form': ItemForm()})


def new_list(request):
    ''' new list '''
    list_ = List.objects.create()
    try:
        item = Item.objects.create(text=request.POST['text'], list=list_)
        item.full_clean()
        item.save()
        return redirect(list_)
    except ValidationError: 
        list_.delete()
        error = "You can't have an empty list item"
        return render(request, 'home.html', {'error': error}) 
    return redirect(list_)

def view_list(request,list_id):
    ''' view list '''
    list_ = List.objects.get(id=list_id)
    error = None
    
    if request.method == "POST":
        try:
            item = Item.objects.create(text=request.POST['text'], list=list_)
            item.full_clean()
            item.save()
            return redirect(list_)
        except ValidationError:
            item.delete()
            error = "You can't have an empty list item"
    return render(request, 'list.html', {'list': list_, 'error': error})




