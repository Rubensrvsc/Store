from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    
    path('producttypes',ProductTypeView.as_view(),name="product_type"),
    path('productcategories',ProductCategoryView.as_view(),name="product_category"),
    path('products',ProductView.as_view(),name="product"),
]