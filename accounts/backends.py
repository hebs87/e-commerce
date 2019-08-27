from django.contrib.auth.models import User


class EmailAuth:
    '''
    Authenicate user by exact match on email and password
    '''
    def authenticate(self, username=None, password=None):
        '''
        Get instance of User based on email and verify password
        '''
        try:
            # username is the name of the form element
            user = User.objects.get(email=username)
            
            # Check password and return user if validation passes
            if user.check_password(password):
                return user
            return None
        # If user doesn't exist, we'll return None
        except User.DoesNotExist:
            return None

    
    def get_user(self, user_id):
        '''
        Used by Django auth system to retrieve user instance
        '''
        try:
            # Django needs primary key for the user
            user = User.objects.get(pk=user_id)
            # If this is an active user
            if user.is_active:
                return user
            return None
        except User.DoesNotExist:
            return None