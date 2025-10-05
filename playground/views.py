from django.shortcuts import render
from store.models import Product
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
    query_set = (
    Product.objects
        # Select specific fields to return as dictionaries
        .values('id', 'title', 'orderitem__product_id')  
        
        # Compare product.id with related orderitem.product_id using F expression
        .filter(id=F('orderitem__product_id'))           
        
        # Sort results alphabetically by product title
        .order_by('title')                              
        
        # Remove duplicates from the result set
        .distinct()                                      
    )


    return render(request, 'hello.html', {'name': 'Mosh', 'products': list(query_set)})
