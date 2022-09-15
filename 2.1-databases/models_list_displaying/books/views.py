from re import template
from django.shortcuts import render, redirect
from .models import Book
from django.http import HttpResponse

def index(request):
    return redirect('books')

def books_view(request):
    template = 'books/books_list.html'
    books = Book.objects.all()
    dates = [f'{date.pub_date}' for date in books]
    dates = list(set(dates))
    dates.sort()
    date = dates[0]
    context = {
        'books': books,
        'pub_date': date
    }
    return render(request, template, context)

def books_by_date(request, pub_date):
    template = 'books/books_pub_date.html'
    dates = [f'{date.pub_date}' for date in Book.objects.all()]
    dates = list(set(dates))
    dates.sort()
    next_date = None
    previous_date = None
    books = Book.objects.filter(pub_date=pub_date)
    
    if int(dates.index(pub_date)) + 1 < int(len(dates)):
        next_date = dates[dates.index(pub_date)+1]
    
    if int(dates.index(pub_date)) - 1 >= 0:
        previous_date = dates[dates.index(pub_date)-1]
    
    
    context = {
        'books': books,
        'next_date': next_date,
        'previous_date': previous_date,
    }
    return render(request, template, context)

def show_book(request, pub_date, slug):
    template='books/book_page.html'
    
    book = Book.objects.get(slug=slug)
    context = {'book': book}
    return render(request, template, context)
