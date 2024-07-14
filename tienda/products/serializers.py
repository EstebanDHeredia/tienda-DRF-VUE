from rest_framework import serializers
from django_filters import rest_framework as filter # django_filters is a Django application used for filtering querysets dynamically. It allows you to create reusable filters for your Django models.
from .models import Product, Category

# ProductFilter es una clase que define filtros para el modelo Product.
class ProductFilter (filter.FilterSet):
    class Meta:
        model = Product
        fields = ['category',] # Voy a filtrar por el campo category
        
class ProductSerializer(serializers.ModelSerializer):
    category_name = serializers.ReadOnlyField(source="category.name") # Creo este campo, para poder mostrar el nombre de la categoria al
    # exportar la api. Lo tengo que agregar en la lista 'fields' de abajo, pero como yo tengo puesto "__all__" no hace falta
    price_type_description = serializers.ReadOnlyField(source="get_price_type_display") # este campo me sirve para mostrar el tipo de precio que tiene el producto, pero en un modo
    # entendible para el usuario. el price_type es del tipo choice: ('media-doc', 'Media Docena') es decir una tupla con el nombre-descripcion. Llamando al metodo get_<nombre_del_campo>_display
    # muestro la parte de la descripcion de la tupla 
    
    class Meta:
        model = Product
        
        # Le indico que campos del modelo Product quiero que me serialice
        # fields = ['id', 'name', 'description', 'price'] # Esto es lo mismo que la linea de abajo
        fields = '__all__'  # TENER CUIDADO CON ESTO, PORQUE PUEDE LLEGAR A MOSTRAR CAMPOS QUE NO QUIERO PUBLICAR
        filterset_class = ProductFilter # Le indico que clase voy a utilizar para el filtrado en este serializer


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'