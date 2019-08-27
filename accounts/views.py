from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib import auth, messages
from django.core.urlresolvers import reverse
from django.template.context_processors import csrf
# To prevent users from getting to unwanted pages when logged out
from django.contrib.auth.decorators import login_required
from .forms import UserLoginForm, UserRegistrationForm

# Create your views here.
def index(request):
    '''
    Return the index.html file
    '''
    return render(request, "index.html")


# Used to ensure user redirected to login page if attempting
# to access when logged out
@login_required
def logout(request):
    '''
    Log the user out
    '''
    auth.logout(request)
    # Display a flash message when user is logged out
    messages.success(request, "You have successfully been logged out")
    # Reverse allows to redirect to url name rather than html file or function
    return redirect(reverse('index'))


def login(request):
    '''
    Return a login page
    '''
    # Ensures that user redirected to index if accessing login,
    # when already logged in
    if request.user.is_authenticated():
        return redirect(reverse('index'))
    
    # If request method is POST, we want to validate login details
    if request.method == "POST":
        # Create an instance of login form and pass POST request as constructor
        login_form = UserLoginForm(request.POST)
        
        if login_form.is_valid():
            # If form is valid, we get both entered username and password
            user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password'])
            
            if user:
                # If details are valid, log user in and display message
                auth.login(request, user)
                messages.success(request, 'You have successfully logged in!')
                # Redirect user to home page once logged in
                if request.GET and request.GET['next'] !='':
                    next = request.GET['next']
                    return HttpResponseRedirect(next)
                else:
                    return redirect(reverse('index'))
            else:
                # If details don't match, display error message
                login_form.add_error(None, 'Your username or password is \
                                     incorrect!')

    else:
        # Else, we want to return a blank form
        login_form = UserLoginForm()
    
    args = {'login_form': login_form, 'next': request.GET.get('next', '')}

    return render(request, "login.html", args)


@login_required
def user_profile(request):
    '''
    The user's profile page
    '''
    return render(request, 'profile.html')


def registration(request):
    '''
    Render the registration page
    '''
    # Ensures that user redirected to index if accessing login,
    # when already logged in
    if request.user.is_authenticated():
        return redirect(reverse('index'))

    if request.method == "POST":
        registration_form = UserRegistrationForm(request.POST)

        if registration_form.is_valid():
            # If form is valid, save user's
            registration_form.save()

            # Authenicate user, save details against relevant field
            user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password1'])
            
            # Log user in if all checks out
            if user:
                auth.login(request, user)
                messages.success(request, 'You have successfully registered!')
                return redirect(reverse('index'))
            else:
                messages.error(request, 'Unable to register your account at \
                               this time!')

    else:
        registration_form = UserRegistrationForm()

    args = {'registration_form': registration_form}

    return render(request, "registration.html", args)
