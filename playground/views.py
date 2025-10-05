from django.shortcuts import render
from store.models import Product
from store.models import Order
from django.http import HttpResponse
from django.db.models import Q,F


def say_hello(request):
    # return query set don't execute immediately
    # query_sets = Product.objects.all() 
    # product = Product.objects.get(pk=0) 
    # product = Product.objects.filter(pk=0).exists()
    # product = Product.objects.filter(unit_price__gt=20)
    # query_set = Product.objects.filter(unit_price__range=(0, 20))
    # query_set = Product.objects.filter(unit_price__lt=20,unit_price__gt=10)
    # query_set = Product.objects.filter(Q(unit_price__lt=20) | Q(unit_price__lt=20))
    # query_set = Product.objects.order_by('-title')[:10]
    # query_set = Product.objects.all().order_by('title')
    # # query_set = Product.objects.order_by('-title')[:10]
    # query_set = Product.objects.all().values('title', 'collection__title')
    # Get a list of unique products where the product's id matches its related order item product_id
    # query_set = (
    # Product.objects
    #     # Select specific fields to return as dictionaries
    #     .values('id', 'title', 'orderitem__product_id')  
        
    #     # Compare product.id with related orderitem.product_id using F expression
    #     .filter(id=F('orderitem__product_id'))           
        
    #     # Sort results alphabetically by product title
    #     .order_by('title')                              
        
    #     # Remove duplicates from the result set
    #     .distinct()                                      
    # )

    # # Example: Using only() and defer() in Django ORM
    # product = Product.objects.only('id', 'title').first()
    # # Loads only 'id' and 'title' fields immediately from the database
    # # Other fields (like 'description', 'price', etc.) will be loaded **lazily** only when accessed

    # product2 = Product.objects.defer('description', 'unit_price').first()
    # # Loads all fields **except** 'description' and 'unit_price' initially
    # # The deferred fields are fetched **only when accessed later**

    # Fetch all products and their related collection in a single SQL query
    # query_set = Product.objects.select_related('collection').all()
    # ✅ select_related() is used for one-to-one or many-to-one relationships (like ForeignKey)
    # ✅ It performs an SQL JOIN to get related 'collection' data immediately
    #used in one-to-one relationship

    # query_set = Product.objects.prefetch_related('promotions').all()
    
    #aggregating objects
    query_set = (
        Order
        .objects
        .select_related('customer')
        .prefetch_related('orderitem_set__product')
        .order_by('-placed_at')[:5]
        )



    return render(request, 'hello.html', {'name': 'Mosh', 'products': list(query_set)})
