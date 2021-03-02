from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    
    path('producttypes',ProductTypeView.as_view(),name="product_types"),
    path('productcategories',ProductCategoryView.as_view(),name="product_categories"),
    path('products',ProductView.as_view(),name="products"),
]