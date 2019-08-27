from django.db import models

# Create your models here.
class Product(models.Model):
    '''
    Our Product model/database
    '''
    name = models.CharField(max_length=254, default='')
    description = models.TextField()
    # Specify max digits and decimal places for decimal field
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='images')
    
    
    def __str__(self):
        return self.name
