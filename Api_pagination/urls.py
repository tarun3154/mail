# pagination_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.product_list, name='product_list'),
    # Add more URL patterns for other front-end views if needed
]
