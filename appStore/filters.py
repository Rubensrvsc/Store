from .models import *
import django_filters

class ProductFilter(django_filters.rest_framework.FilterSet):

    price = django_filters.rest_framework.NumberFilter(field_name="price_one", lookup_expr=['gte','lte'])

    class Meta:
        model = Product
        fields = ['price']