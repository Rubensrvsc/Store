from .models import *
from rest_framework import serializers
from rest_framework.reverse import reverse

class ProductTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductType
        fields = ['name_product_type']

class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'

class ProductCategoryListSerializer(serializers.ModelSerializer):

    product = serializers.SerializerMethodField()

    class Meta:
        model = ProductCategory
        fields = ['id','name_product_category','product']

    def get_product(self,instance):
        return Product.objects.all().values('name_product','color','price')

class ProductListSerializer(serializers.ModelSerializer):

    product_size = serializers.PrimaryKeyRelatedField(source='product_size.size',queryset=Size.objects.all())
    product_type = serializers.PrimaryKeyRelatedField(source='product_type.name_product_type',queryset=ProductType.objects.all())
    product_category = serializers.PrimaryKeyRelatedField(source='product_category.name_product_category',queryset=ProductCategory.objects.all())


    class Meta:
        model = Product
        fields = ['name_product','color','price','product_category','product_size','product_type']

    
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

class SearchProductNameSerializer(serializers.Serializer):

    name_search_product = serializers.CharField()

    def validate_name_search_product(self, data):
        if data is None:
            raise serializers.ValidationError({'error':'name is empty'})
        return data



class SearchProductPriceSerializer(serializers.Serializer):
    price_one = serializers.FloatField()
    price_two = serializers.FloatField()

    
    