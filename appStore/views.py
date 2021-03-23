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
from django.db.models import Q
from rest_framework import filters

# Create your views here.

@api_view(['GET'])
def api_root(request,format=None):
    return Response({
        'products': reverse('api:products',request=request,format=format),
        'create product': reverse('api:create_product',request=request,format=format),
        'search product': reverse('api:search-product',request=request,format=format),
        'product type': reverse('api:product_types',request=request,format=format),
        'create size': reverse('api:size-list-create',request=request,format=format),
        'product category': reverse('api:product_categories',request=request,format=format),
        'create category': reverse('api:create-category',request=request,format=format),
    })

class ProductTypeView(generics.ListCreateAPIView):
    queryset = ProductType.objects.all()
    serializer_class = ProductTypeSerializer

class ProductCategoryView(generics.ListAPIView):
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategoryListSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name_product_category']

class ProductCategoryCreateView(generics.CreateAPIView):
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategoryCreateSerializer

class SizeListCreateView(generics.ListCreateAPIView):
    queryset = Size.objects.all()
    serializer_class = SizeSerializer

    def get(self, request, *args, **kwargs):
        return Response(status=status.HTTP_200_OK)

class ProductView(generics.ListAPIView):
    lookup_field = "id"
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer
    pagination_class = PageNumberPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['name_product','price']

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



class SearchPriceProductView(APIView):
    queryset = Product.objects.all()

    def get(self,request,*args,**kwargs):
        if float(self.kwargs["price_one"]) <= 0:
            raise serializers.ValidationError({'error':'Price one is empty or less the zero'})
        elif float(self.kwargs["price_two"]) <= 0:
            raise serializers.ValidationError({'error':'Price two is empty or less the zero'})
        elif float(self.kwargs["price_one"]) > float(self.kwargs["price_two"]):
            raise serializers.ValidationError({'error':'Price one more than price two'})
        
        price_one = float(self.kwargs["price_one"])
        price_two = float(self.kwargs["price_two"])
        
        query = self.queryset.filter(Q(price__gte=price_one) & Q(price__lte=price_two)).values(
            'name_product','color','price',
            'product_size__size','product_category__name_product_category',
            'product_type__name_product_type'
        )
        return Response(query)

 