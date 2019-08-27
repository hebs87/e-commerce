from django.shortcuts import render
from .models import Product

# Create your views here.
def all_products(request):
    '''
    Returns all products
    '''
    products = Product.objects.all()
    # Render html file and we will have access to all products
    return render(request, 'products.html', {'products': products})
