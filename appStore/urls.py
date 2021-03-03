from django.contrib import admin
from django.urls import path
from .views import *
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = format_suffix_patterns([
    
    path('producttypes',ProductTypeView.as_view(),name="product_types"),
    path('productcategories',ProductCategoryView.as_view(),name="product_categories"),
    path('products',ProductView.as_view(),name="products"),
    path('products/<int:id>',ProductDetailView.as_view(),name="product-detail"),
    path('updateproduct/<int:id>',ProductUpdateView.as_view(),name="update-product"),
    path('',api_root,name="api_root"),
])