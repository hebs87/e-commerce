from django.shortcuts import get_object_or_404
from products.models import Product


def cart_contents(request):
    '''
    Ensures that the cart contents are available when rendering every page
    '''
    # Requests exisiting cart if there is one, or blank dict if not
    cart = request.session.get('cart', {})
    
    # Initialize cart_items, total and product count
    cart_items = []
    total = 0
    product_count = 0
    
    # For loop to loop through each id and quantity of item in cart
    for id, quantity in cart.items():
        # Get product from Product model by its ID
        product = get_object_or_404(Product, pk=id)
        # Keep running total of quantity of product * price
        total += quantity * product.price
        # Product count keeps adding the quantity
        product_count += quantity
        # Append each item to the cart
        cart_items.append({'id': id, 'quantity': quantity, 'product': product})
    
    # Return dict with k,v pairs for cart_items, total and product_count
    return { 'cart_items': cart_items, 'total': total, 'product_count': product_count }
