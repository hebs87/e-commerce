from django.shortcuts import render
from products.models import Product

# Create your views here.
def do_search(request):
    '''
    Allows user to search for a product by its name
    '''
    # Filters products based on the form entry
    # 'q' is the input field's name in the form
    products = Product.objects.filter(name__icontains=request.GET['q'])
    return render(request, "products.html", {'products': products})
