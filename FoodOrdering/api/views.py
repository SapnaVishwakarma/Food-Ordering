from django.shortcuts import render
from rest_framework import viewsets
from api.models import Product
from api.serializers import ProductSerializer

# Create your views here.
class ProductViewSet(viewsets.ModelViewSet()):
    querysets=Product.object.all()
    serializer_class=ProductSerializer
