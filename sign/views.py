from django.shortcuts import render
from django.views.generic import ListView
from .models import Author, Book

class AuthorListView(ListView):
    model = Author
    template_name = 'sign/author_list.html'
    context_object_name = 'authors'

class BookListView(ListView):
    model = Book
    template_name = 'sign/book_list.html'
    context_object_name = 'books'
