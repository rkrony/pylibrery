from django.http import Http404
from django.shortcuts import render
from django.http import HttpResponse
from .models import Book


def index(request):
    all_book = Book.objects.all()
    context = {
        "all_book" : all_book
    }

    return render(request,'book/index.html', context)

def details(request,book_id):
    try:
        book = Book.objects.get(id=book_id)
    except Book.DoesNotExist:
        raise Http404('This book does not exist')
    return render(request, 'book/details.html', {'book': book})