from django.shortcuts import render, redirect, reverse


# Create your views here.
def view_cart(request):
    '''
    A view that renders the cart contents page
    '''
    # No need to pass in dict of cart_contents as context available everywhere
    return render(request, "cart.html")


def add_to_cart(request, id):
    '''
    Add a quantity of the specified product to the cart
    '''
    # Takes int - gets it from quantity form on products page
    # Allows to increase/decrease number
    # When click 'ADD', int in form will go into cart
    quantity = int(request.POST.get('quantity'))
    # Gets cart from the session if there is one, or empty dict if not
    cart = request.session.get('cart', {})
    # Add ID and quantity to cart
    if id in cart:
        # If item is already in cart, we add the new quantiy to existing
        cart[id] = int(cart[id]) + quantity
    else:
        # If item not in cart, existing value is overwritten
        cart[id] = cart.get(id, quantity)

    request.session['cart'] = cart
    return redirect(reverse('index'))


def adjust_cart(request, id):
    '''
    Adjust the quantity of the specified product to the specified amount
    '''
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})
    
    # Adjust the quantity
    # Can only adjust the amount if quantity is greater than 0
    if quantity > 0:
        cart[id] = quantity
    else:
        cart.pop(id)

    # Redirect to our view_cart view
    request.session['cart'] = cart
    return redirect(reverse('view_cart'))
