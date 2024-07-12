from django.shortcuts import render
from rest_framework import generics # Este modulo me provee una lista de vistas genéricas para listar, actualizar, crear y borrar datos
from .models import Product
from .serializers import ProductSerializer

# Create your views here.
# Esta clase me permite listar y crear productos
class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

# Esta vista me permite mostrar, actualizar y eliminar porductos
class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
