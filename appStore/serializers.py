from .models import *
from rest_framework import serializers
from rest_framework.reverse import reverse

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

    def validate_price(self, data):
        if data < 0:
            raise serializers.ValidationError({"error": "Price less than zero"})
        return data
    
class ProductUpdateSerializer(serializers.ModelSerializer):

    name_product = serializers.CharField(required=False)
    color = serializers.CharField(required=False)
    price = serializers.FloatField(required=False)

    class Meta:
        model = Product
        fields = ['name_product','color','price']
    
    def validate_price(self, data):
        if data < 0:
            raise serializers.ValidationError({"error": "Price less than zero"})
        return data
    