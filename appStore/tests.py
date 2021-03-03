from django.test import TestCase
from rest_framework.test import APIRequestFactory, APIClient
from .models import *
from rest_framework import status
# Create your tests here.

class ProductTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        pass
