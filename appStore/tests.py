from django.test import TestCase
from rest_framework.test import APIRequestFactory, APIClient
from .models import *
from rest_framework import status
# Create your tests here.

class ProductCategoryTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        ProductCategory.objects.create(name_product_category="Infantil")
        ProductCategory.objects.create(name_product_category="Adulto")
        ProductCategory.objects.create(name_product_category="Idoso")

    def test_create_product_category(self):
        factory = APIClient()
        product_category = {"name_product_category": "infantil"}
        request = factory.post('/createcategory',product_category)
        self.assertEquals(request.status_code,status.HTTP_201_CREATED)

    def test_list_product_category(self):
        factory = APIClient()
        products_categories = ProductCategory.objects.all().count()
        request = factory.get("/productcategories")
        self.assertEquals(products_categories,3)
