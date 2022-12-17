from django.shortcuts import render
from .models import Product
from django.http import JsonResponse
from .serializer import ProductSerializer


def index(req):
    return JsonResponse('hello', safe=False)


def myProducts(req):
    all_products = ProductSerializer(Product.objects.all(), many=True).data
    return JsonResponse(all_products, safe=False)