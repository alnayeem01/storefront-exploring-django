from django.db import models

# Create your models here.
class store(models.Model):
    #django creates unique id automatically, 
    #But we can set it manually by writing the following code 
    sku = models.CharField(max_length=10, primary_key=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.IntegerField()
    last_update = models.DateTimeField(auto_now=True)

class Customer(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.TextField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.models.CharField( max_length=255)
    birth_date = models.DateField(null = True) # mensa the field can be null
