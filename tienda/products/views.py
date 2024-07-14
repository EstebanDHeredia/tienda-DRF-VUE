from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action #The action decorator is used in Django REST Framework to define custom view methods for API views. It allows you to add additional HTTP methods to your API endpoints.
from rest_framework.response import Response #  module used to return responses in Django REST framework views.
from rest_framework import generics # Este modulo me provee una lista de vistas genéricas para listar, actualizar, crear y borrar datos
from .models import Product, Category
from .serializers import ProductSerializer, CategorySerializer

# Create your views here.
# # Esta clase me permite listar y crear productos
# class ProductList(generics.ListCreateAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer

# # Esta vista me permite mostrar, actualizar y eliminar porductos
# class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    def get_queryset(self):
        queryset = super().get_queryset()
        category = self.request.query_params.get('category')
        if category:
            queryset = queryset.filter(category=category)
        return queryset
    
    # Este filtro lo reemplacé por la definición de arriba de get_queryset arriba
    # @action(detail=False)
    # def by_category(self, request):
    #     category = self.request.query_params.get('category', None) # Asigna el valor del parámetro de consulta 'category' de la solicitud
    #                                                                 #a la variable 'category'. Si el parámetro de consulta 'category' 
    #                                                                 # no está presente en la solicitud, asigna el valor 'None' a la variable.
    #                                                                 # Es decir, en un ruta 'http://127.0.0.1:8000/api/products/by_category/?category=1'
    #                                                                 # busca el valor despues de ?category= y se lo asigna a la variable category
    #     products = Product.objects.filter(category = category)
    #     serializer = ProductSerializer(products, many = True) # creates a ProductSerializer instance and passes the filtered products queryset to it. The many=True argument indicates that the serializer should expect a list of objects.
    #     return Response(serializer.data)
    
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
