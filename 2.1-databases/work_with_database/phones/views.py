from django.shortcuts import render, redirect
from .models import Phone

def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    sort_type = str(request.GET.get('sort'))

    if sort_type == 'name':
        phones = Phone.objects.order_by('name')[0:]
    elif sort_type == 'min_price':
        phones = Phone.objects.order_by('price')[0:]
    elif sort_type == 'max_price':
        phones = Phone.objects.order_by('-price'[0:])
    else:
        phones = Phone.objects.all()

    context = {'phones': phones}

    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'

    phone = Phone.objects.get(slug=slug)
    context = {'phone': phone}
    return render(request, template, context)
