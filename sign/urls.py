from django.urls import path
from . import views

urlpatterns = [
    path('authors/', views.AuthorListView.as_view(), name='author-list'),
    path('books/', views.BookListView.as_view(), name='book-list'),
]
