from django.shortcuts import redirect, render
from django.http import HttpResponse
from lists.models import Item


def home_page(request):
    '''home page'''

    if request.method == "POST":
        new_item_text = request.POST['item_text']
        Item.objects.create(text=new_item_text)
        return redirect('/lists/one-of-the-world/')

    items = Item.objects.all()

    return render(request, 'home.html')


def view_list(request):
    ''' view list '''
    items = Item.objects.all()
    return render(request, 'list.html', {'items': items})

