from django.db import models
from products.models import Product

# Create your models here.
class Order(models.Model):
    '''
    Gives a summary of the user's order
    '''
    # blank=False means it can't be left blank
    full_name = models.CharField(max_length=50, blank=False)
    phone_number = models.CharField(max_length=20, blank=False)
    street_address1 = models.CharField(max_length=40, blank=False)
    street_address2 = models.CharField(max_length=40, blank=False)
    town_or_city = models.CharField(max_length=40, blank=False)
    county = models.CharField(max_length=40, blank=False)
    country = models.CharField(max_length=40, blank=False)
    postcode = models.CharField(max_length=20, blank=True)
    date = models.DateField()


    def __str__(self):
        # Summary of the order
        return "{0}-{1}-{2}".format(self.id,
                                    self.date,
                                    self.full_name)


class OrderLineItem(models.Model):
    '''
    Each order line item - gets the foreign key from the Order model above
    Also gets the foreign key from the Product model we imported
    '''
    order = models.ForeignKey(Order, null=False)
    product = models.ForeignKey(Product, null=False)
    quantity = models.IntegerField(blank=False)


    def __str__(self):
        # Returns string showing the number of the product at its price
        return "{0} {1} @ {2}".format(self.quantity,
                                      self.product.name,
                                      self.product.price)