from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import Product
from .serializers import ProductSerializer
from rest_framework.response import Response

# Create your views here.

@api_view(["GET"])
def products(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)

@api_view(["GET"])
def product_detail(request, slug):
    products = Product.objects.get(slug=slug)  
    serializer = DetailedProductSerializer(product)
    return Response(serializer.data)