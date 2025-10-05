from django.db import models


class Promotion(models.Model):
    description = models.CharField(max_length=255)
    discount = models.FloatField()


class Collection(models.Model):
    title = models.CharField(max_length=255)
    featured_product = models.ForeignKey(
        'Product', on_delete=models.SET_NULL, null=True, related_name='+')


class Product(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    description = models.TextField()
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.IntegerField()
    last_update = models.DateTimeField(auto_now=True)
    collection = models.ForeignKey(Collection, on_delete=models.PROTECT)
    promotions = models.ManyToManyField(Promotion)


class Customer(models.Model):
    MEMBERSHIP_BRONZE = 'B'
    MEMBERSHIP_SILVER = 'S'
    MEMBERSHIP_GOLD = 'G'

    MEMBERSHIP_CHOICES = [
        (MEMBERSHIP_BRONZE, 'Bronze'),
        (MEMBERSHIP_SILVER, 'Silver'),
        (MEMBERSHIP_GOLD, 'Gold'),
    ]
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=255)
    birth_date = models.DateField(null=True)
    membership = models.CharField(
        max_length=1, choices=MEMBERSHIP_CHOICES, default=MEMBERSHIP_BRONZE)


    # This is an inner Meta class inside a Django model. It lets you add extra settings about how the model behaves with the database.
    class Meta:
        """
        - `Meta` lets you customize model behavior.
        - `db_table`: rename the actual SQL table (default would be app_model).
        - `indexes`: create DB indexes for faster queries.
        Example: searching customers by first_name + last_name will be quick.

        By default, Django would name the table <appname>_<modelname> → e.g. store_customer.
        With db_table, you override that default.
        Here, you’re telling Django:
        👉 “Instead of store_customer, create/use a table called store_customers.

        """
        db_table ='store_customers'
        indexes = [
            models.Index(fields=['first_name', 'last_name'])
        ]

class Order(models.Model):
    PAYMENT_STATUS_PENDING = 'P'
    PAYMENT_STATUS_COMPLETE = 'C'
    PAYMENT_STATUS_FAILED = 'F'
    PAYMENT_STATUS_CHOICES = [
        (PAYMENT_STATUS_PENDING, 'Pending'),
        (PAYMENT_STATUS_COMPLETE, 'Complete'),
        (PAYMENT_STATUS_FAILED, 'Failed')
    ]

    placed_at = models.DateTimeField(auto_now_add=True)
    payment_status = models.CharField(
        max_length=1, choices=PAYMENT_STATUS_CHOICES, default=PAYMENT_STATUS_PENDING)
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)


class Address (models.Model):
# address ahd one to one relationship with custoemr -( a customer can have one address, a address can have one customer)
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    # - on_delete=CASCADE: delete address if customer is deleted
    # - primary_key=True: use customer_id as primary key (no separate id)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

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
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory  = models.IntegerField()
    last_update = models.DateTimeField(auto_now=True)
    # one Collection : many Product
    collection = models.ForeignKey(Collection, on_delete=models.RESTRICT)
    # many Product : many Promotions
    promotions = models.ManyToManyField(Promotion)




class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.PROTECT)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.PositiveSmallIntegerField()
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)


class Address(models.Model):
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    customer = models.ForeignKey(
        Customer, on_delete=models.CASCADE)


class Cart(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField()
