from django.conf.urls import url
from .views import view_cart, add_to_cart, adjust_cart

urlpatterns = [
    url(r'^$', view_cart, name="view_cart"),
    # Links to the add button on the products page
    url(r'^add/(?P<id>\d+)', add_to_cart, name="add_to_cart"),
    # Links to the adjust button within the cart itself
    url(r'^adjust/(?P<id>\d+)', adjust_cart, name="adjust_cart"),
]