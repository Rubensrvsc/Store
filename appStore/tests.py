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

        
        ProductType.objects.create(name_product_type="camisa")
        ProductType.objects.create(name_product_type="calça")
        
        Size.objects.create(size="GG")
        Size.objects.create(size="G")
        
        size = Size.objects.get(id=1)
        category_product = ProductCategory.objects.get(id=1)
        type_product = ProductType.objects.get(id=1)

        Product.objects.create(
            name_product="camisa 1",
            price=100,
            color="red",
            product_category = category_product,
            product_size = size,
            product_type = type_product
        )


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

    def test_create_product(self):
        factory = APIClient()
        
        size = Size.objects.get(id=1)
        category_product = ProductCategory.objects.get(id=1)
        type_product = ProductType.objects.get(id=1)
        

        product = {'name_product':"camisa 1",
            'price':100,
            'color':"red",
            'product_category' : category_product.id,
            'size': size.id,
            'product_type': type_product.id
            }
        response = factory.post('/create_product',product)
        self.assertEquals(response.status_code,status.HTTP_301_MOVED_PERMANENTLY)


    

