from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework.response import Response

# Create your views here.

@api_view(['GET'])
def api_root(request,format=None):
    return Response({
        'products': reverse('products',request=request,format=format),
        'product type': reverse('product_types',request=request,format=format),
        'product category': reverse('product_categories',request=request,format=format),
    })

class ProductTypeView(generics.ListCreateAPIView):
    queryset = ProductType.objects.all()
    serializer_class = ProductTypeSerializer

class ProductCategoryView(generics.ListCreateAPIView):
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer

class ProductView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDetailView(generics.RetrieveAPIView):
    lookup_field = "id"
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductUpdateView(generics.UpdateAPIView):
    lookup_field = "id"
    queryset = Product.objects.all()
    serializer_class = ProductUpdateSerializer


