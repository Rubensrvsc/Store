from .models import *
from rest_framework import serializers

class ProductTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductType
        fields = '__all__'

class ProductCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductCategory
        fields = '__all__'