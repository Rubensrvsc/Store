from .models import *
from rest_framework import serializers

class ProductTypeSerializer(serializers.ModelSerializer):


    class Meta:
        model = ProductType
        fields = ['name_product_type']

class ProductCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductCategory
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ['name_product','color','price','product_category','product_size','product_type']