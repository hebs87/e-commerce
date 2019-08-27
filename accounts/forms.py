from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError


# Create a new form object
class UserLoginForm(forms.Form):
    '''
    Form to be used to log users in
    '''
    username = forms.CharField()
    # widget of password input ensures field has input type of password
    password = forms.CharField(widget=forms.PasswordInput)


class UserRegistrationForm(UserCreationForm):
    '''
    Form used to create a new user
    '''
    # First password entry
    password1 = forms.CharField(label="Password",
                                widget=forms.PasswordInput)
    # Confirm password with a label
    password2 = forms.CharField(label="Confirm Password",
                                widget=forms.PasswordInput)
    # Create inner class to give more info about fomr - model and fields
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


    # clean_ validates field and returns clean data which we can verify
    # Expects to return specified value when done
    def clean_email(self):
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        # Check the email doesn't already exist in the DB using filter
        if User.objects.filter(email=email).exclude(username=username):
            raise forms.ValidationError(u'Email address must be unique')
        return email
    
    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')


        # Check to see if either is None - they aren't entered
        if not password1 or not password2:
            raise forms.ValidationError(u'Please confirm your password')

        # Check that both passwords match
        if password1 != password2:
            raise forms.ValidationError(u'Passwords must match')

        return password2
