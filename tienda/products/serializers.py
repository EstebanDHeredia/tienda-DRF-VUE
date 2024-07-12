from rest_framework import serializers
from .models import Product, Category

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        
        # Le indico que campos del modelo Product quiero que me serialice
        # fields = ['id', 'name', 'description', 'price'] # Esto es lo mismo que la linea de abajo
        fields = '__all__'  # TENER CUIDADO CON ESTO, PORQUE PUEDE LLEGAR A MOSTRAR CAMPOS QUE NO QUIERO PUBLICAR


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'