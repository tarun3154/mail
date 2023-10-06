from django.shortcuts import render
from django.core.paginator import Paginator
from faker import Faker

fake = Faker()

def generate_dummy_data(num_records):
    dummy_data = []
    for _product in range(num_records):
        product = {
            'title': fake.word(),
            'description': fake.sentence(),
            'price': fake.random_number(2, 1000),
        }
        dummy_data.append(product)
        
    return dummy_data

def product_list(request):
    dummy_product_list = generate_dummy_data(100)  # Generate 100 dummy products
    paginator = Paginator(dummy_product_list, 10)  # Show 10 products per page
    page1 = request.GET.get('page')
    page = paginator.get_page(page1)
    
    
    return render(request, 'Api_pagination/product_list.html', {'page': page})
