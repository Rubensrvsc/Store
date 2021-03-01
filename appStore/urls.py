from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    
    path('producttypes',ProductTypeView.as_view(),name="product_type"),
    path('productcategory',ProductCategoryView.as_view(),name="product_category"),
]