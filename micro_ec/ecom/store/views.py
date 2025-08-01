from django.shortcuts import render , get_object_or_404
from .models import Product

# Create your views here.

def product_list(request):
    products = Product.objects.all()
    return render(request , "store/product_list.html" , {"products" : products})

def product_detail(request , pk):
    product = get_object_or_404(product , pk = pk)
    return render(request , 'store/product_list.html'  , {"product" : product})