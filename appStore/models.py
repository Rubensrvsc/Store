from django.db import models

# Create your models here.

class ProductType(models.Model):
    name_product_type = models.CharField(max_length=30)

    def __str__(self):
        return self.name_product_type

class Size(models.Model):
    size = models.CharField(max_length=30)

    def __str__(self):
        return self.size
    
class ProductCategory(models.Model):
    name_product_category = models.CharField(max_length=30)

    def __str__(self):
        return self.name_product_category
    
class Product(models.Model):
    name_product = models.CharField(max_length=100)
    color = models.CharField(max_length=30)
    price = models.FloatField()
    product_category = models.ForeignKey(ProductCategory, related_name="category_product",on_delete=models.CASCADE)
    product_size = models.ForeignKey(Size, related_name="size_product",on_delete=models.CASCADE)
    product_type = models.ForeignKey(ProductType, related_name="type_product",on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name_product