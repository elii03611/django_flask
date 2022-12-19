from django.shortcuts import render
from .models import Product
from django.http import JsonResponse
from .serializer import ProductSerializer
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated


def index(req):
    return JsonResponse('hello', safe=False)

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['username'] = user.username
        return token
 
 
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def myProducts(req):
    all_products = ProductSerializer(Product.objects.all(), many=True).data
    return JsonResponse(all_products, safe=False)
