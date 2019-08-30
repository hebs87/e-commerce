from django import forms
from .models import Order

class MakePaymentForm(forms.Form):
    '''
    Form for the user to make payment
    '''
    # For card expiry date, create dropdown options
    MONTH_CHOICES = [(i, i) for i in range(1, 12)]
    # This needs to be maintained/updated each year
    YEAR = [(i, i) for i in range(2019, 2036)]

    # required=False makes it more secure and lets Stripe deal with encryption
    # Ensures plain text not transmitted through the browser
    credit_card_number = forms.CharField(label='Credit card number', required=False)
    cvv = forms.CharField(label='Security code (CVV)', required=False)
    expiry_month = forms.ChoiceField(label='Month', choices=MONTH_CHOICES, required=False)
    expiry_year = forms.ChoiceField(label='Year', choices=YEAR, required=False)
    # Stripe requires an ID - something will be inputted into the form,
    # but will be hidden from the user
    stripe_id = forms.CharField(widget=forms.HiddenInput)

class OrderForm(forms.ModelForm):
    '''
    Form that the user completed for the order
    '''
    class Meta:
        model = Order
        fields = (
            'full_name', 'phone_number', 'street_address1',
            'street_address1', 'town_or_city', 'county','country',
            'postcode'
        )