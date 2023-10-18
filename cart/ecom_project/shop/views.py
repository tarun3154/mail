# shop/views.py
from django.shortcuts import render, redirect
from .models import Product, CartItem

def product_list(request):
    products = Product.objects.all()
    return render(request, 'shop/product_list.html', {'products': products})

def add_to_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    CartItem.objects.create(product=product)
    return redirect('product_list')

def remove_from_cart(request, item_id):
    item = CartItem.objects.get(id=item_id)
    item.delete()
    return redirect('cart')

def view_cart(request):
    cart_items = CartItem.objects.all()
    return render(request, 'shop/cart.html', {'cart_items': cart_items})
