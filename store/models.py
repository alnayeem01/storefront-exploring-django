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

    #memberhsip field with some options. For consistenty we are usign variables
    MEMBERSHIP_BRONZE = "B"
    MEMBERSHIP_SILVER = "S"
    MEMBERSHIP_GOLD ="G"

    MEMBERSHIP_CHOICES = [
        (MEMBERSHIP_BRONZE, 'Bronze'),
        (MEMBERSHIP_SILVER, 'Silver'),
        (MEMBERSHIP_GOLD, 'Gold'),
    ]

    first_name = models.CharField(max_length=255)
    last_name = models.TextField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField( max_length=255)
    birth_date = models.DateField(null = True) # mensa the field can be null
    membership = models.CharField(max_length=1, choices=MEMBERSHIP_CHOICES, default=MEMBERSHIP_BRONZE) #here we passed the options and also the default value 

class Order(models.Model):
    PAYMENT_PENDING = 'P'
    PAYMENT_COMPLETE = 'C'
    PAYMENT_FAILED = 'F'
    PAYMENT_CHOICES = [
        (PAYMENT_PENDING, 'Pending'),
        (PAYMENT_COMPLETE, 'Complete'),
        (PAYMENT_FAILED, 'Failed'),
    ]
    placed_at= models.DateTimeField(auto_now_add=True)
    payment_status = models.CharField(max_length=1, choices=PAYMENT_CHOICES)
    #one customer : many orders
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)


class Address (models.Model):
# address ahd one to one relationship with custoemr -( a customer can have one address, a address can have one customer)
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    # - on_delete=CASCADE: delete address if customer is deleted
    # - primary_key=True: use customer_id as primary key (no separate id)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    zip = models.CharField(max_length=255)

class Promotion(models.Model):
    title = models.CharField(max_length=255)
    discount = models.FloatField()
    
class Collection(models.Model):
    title = models.CharField(max_length=255)
    # 'related_name="+"' disables reverse relation
    # This prevents conflict because Product already links to Collection
    featured_product = models.ForeignKey('Product', on_delete=models.SET_NULL, null=True, related_name='+') #tells django to ignore reverse realtionshi

class Product(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    description = models.TextField()
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory  = models.IntegerField()
    last_update = models.DateTimeField(auto_now=True)
    # one Collection : many Product
    collection = models.ForeignKey(Collection, on_delete=models.RESTRICT)
    # many Product : many Promotions
    promotions = models.ManyToManyField(Promotion)




class OrderItem(models.Model):
    #nridge table for : order and product many to many relationship
    #one Order : many orderItem
    order = models.ForeignKey(Order, on_delete=models.PROTECT)
    #one Product : many orderItem 
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.PositiveSmallIntegerField()
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)

class Cart(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

class cartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField()

