from django.shortcuts import render
from .models import *
from .serializers import *
import json
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView
from django.http import JsonResponse
from rest_framework import status

# Create your views here.

@api_view(['GET'])
def api_root(request,format=None):
    return Response({
        'products': reverse('api:products',request=request,format=format),
        'create product': reverse('api:create_product',request=request,format=format),
        'search product': reverse('api:search-product',request=request,format=format),
        'product type': reverse('api:product_types',request=request,format=format),
        'product category': reverse('api:product_categories',request=request,format=format),
    })

class ProductTypeView(generics.ListCreateAPIView):
    queryset = ProductType.objects.all()
    serializer_class = ProductTypeSerializer

class ProductCategoryView(generics.ListCreateAPIView):
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer

class ProductView(generics.ListAPIView):
    lookup_field = "id"
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer
    pagination_class = PageNumberPagination

class ProductCreateView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDetailView(generics.RetrieveAPIView):
    lookup_field = "id"
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductUpdateView(generics.RetrieveUpdateAPIView):
    lookup_field = "id"
    queryset = Product.objects.all()
    serializer_class = ProductUpdateSerializer

class SearchProductView(APIView):
    queryset = Product.objects.all()
    serializer_class = SearchProductNameSerializer

    def get(self,request):
        return Response(status=status.HTTP_200_OK)

    def post(self,request):
        return JsonResponse(list(self.queryset.filter(name_product__contains=request.data['name_search_product']).values('name_product',
        'color','price','product_size__size','product_category__name_product_category',
        'product_type__name_product_type')),safe=False)
