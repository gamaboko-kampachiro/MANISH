from django.test import TestCase
from .models import Product

# Create your tests here.

class ProdTest(TestCase):
    def test_create_product(self):
        product = Product.objects.create(name='laptop', price=1000.00 , stock = 10)
        self.assertEqual(product.name, 'laptop')