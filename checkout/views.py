from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import MakePaymentForm, OrderForm
from .models import OrderLineItem
from django.conf import settings
from django.utils import timezone
from products.models import Product
import stripe

# Create your views here.
# Import the Stripe Secret API key
stripe.api_key = settings.STRIPE_SECRET


@login_required()
def checkout(request):
    '''
    Allows users to pay for the items that are in their cart
    '''
    if request.method=="POST":
        # Store the order form and payment form details in variables
        order_form = OrderForm(request.POST)
        payment_form = MakePaymentForm(request.POST)
        
        if order_form.is_valid() and payment_form.is_valid():
            # If both forms are valid, order form will be saved as order
            order = order_form.save(commit=False)
            # Order date will be the date that the button was clicked
            order.date = timezone.now()
            order.save()
            
            # Get info for what is being purchased from the cart from session
            cart = request.session.get('cart', {})
            # Initialize total of 0 and then do a for loop to calculate cart total
            total = 0
            for id, quantity in cart.items():
                # Get product ID from the item being purchased
                product = get_object_or_404(Product, pk=id)
                # Calculate total
                total += quantity * product.price
                # Order line item takes the things we've just created
                order_line_item = OrderLineItem(
                    order = order, 
                    product = product, 
                    quantity = quantity
                    )
                # Save the order line item with details for that product
                order_line_item.save()
                
            try:
                # Use stripe's inbuilt API to create a customer and charge
                customer = stripe.Charge.create(
                    amount = int(total * 100),
                    # Stripe uses pence so amount needs to be converted
                    currency = "EUR",
                    # We see the email from the Stripe dashboard
                    description = request.user.email,
                    card = payment_form.cleaned_data['stripe_id'],
                )
            except stripe.error.CardError:
                # Display error message if card is declined
                messages.error(request, "Your card was declined!")
                
            if customer.paid:
                # Display success message, request cart from session &
                # redirect to products page
                messages.success(request, "You have successfully paid")
                request.session['cart'] = {}
                return redirect(reverse('products'))
            else:
                messages.error(request, "Unable to take payment")
        # If order form isn't valid
        else:
            print(payment_form.errors)
            messages.error(request, "We were unable to take a payment with that card!")
    # At the start, before the user pays
    else:
        payment_form = MakePaymentForm()
        order_form = OrderForm()
        
    return render(request, "checkout.html", {'order_form': order_form, 'payment_form': payment_form, 'publishable': settings.STRIPE_PUBLISHABLE})