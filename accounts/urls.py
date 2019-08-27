from django.conf.urls import url, include
from accounts.views import logout, login, registration, user_profile
from accounts import urls_reset


urlpatterns = [
    url(r'^register/$', registration, name="registration"),
    url(r'^profile/$', user_profile, name="profile"),
    url(r'^logout/$', logout, name="logout"),
    url(r'^login/$', login, name="login"),
    # Use include to include the password reset urls
    url(r'^password-reset/', include(urls_reset))
]
