from django.conf.urls import url
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.views import password_reset, password_reset_done, password_reset_confirm, password_reset_complete

#urls
urlpatterns = [
    # Base URL - give some context and redirect to password_reset_done view
    url(r'^$', password_reset,
        {'post_reset_redirect': reverse_lazy('password_reset_done')},
        name='password_reset'),
    url(r'^done/$', password_reset_done, name='password_reset_done'),
    # Contains unique token created for each password reset that is called
    # Has a uid which contains numbers and characters
    # Then create token
    # password_reset_confirm is the url that is normally sent in an email
    # The link then redirects to the post_reset_confirm view
    url(r'^(?P<uidb64>[0-9A-za-z]+)-(?P<token>.+)/$', password_reset_confirm,
        {'post_reset_redirect': reverse_lazy('password_reset_complete')},
        name='password_reset_confirm'),
    url(r'^complete/$', password_reset_complete,
        name='password_reset_complete')
]