from django.shortcuts import render
from django.views.generic import ListView,DetailView
from testApp.models import Book


# Create your views here.

class BookListView(ListView):
    model=Book
    template_name='testAppHtmls/books.html'
    context_object_name='list_of_books'
    #default template :  book_list.html  django contact automatically
    #default context object : book_list


class BookDetailView(DetailView):
    model=Book
    #default template_name : book_detail.html
    #default context : book or object
    #template_name='testAppHtmls/'
