from django.contrib import admin
from django.urls import path
from .views import *
from rest_framework.urlpatterns import format_suffix_patterns

app_name = "api"


urlpatterns = format_suffix_patterns([
    
    path('producttypes',ProductTypeView.as_view(),name="product_types"),
    path('productcategories',ProductCategoryView.as_view(),name="product_categories"),
    path('createcategory',ProductCategoryCreateView.as_view(),name='create-category'),
    path('products',ProductView.as_view(),name="products"),
    path('create_product/',ProductCreateView.as_view(),name="create_product"),
    path('size',SizeListCreateView.as_view(),name='size-list-create'),
    path('products/<int:id>',ProductDetailView.as_view(),name="product-detail"),
    path('updateproduct/<int:id>',ProductUpdateView.as_view(),name="update-product"),
    path('searchpriceproduct/<str:price_one>/<str:price_two>',SearchPriceProductView.as_view(),name="search-price-product"),
    path('searchproduct',SearchProductView.as_view(),name="search-product"),
    path('',api_root,name="api_root"),
])