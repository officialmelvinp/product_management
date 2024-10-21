from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Product

class ProductTests(APITestCase):
    
    # Test for creating a new product
    def test_create_product(self):
        url = reverse('product-list')
        data = {'name': 'Product 1'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Product.objects.count(), 1)
        self.assertEqual(Product.objects.get().name, 'Product 1')
    
    # Test for retrieving a product by ID
    def test_retrieve_product(self):
        product = Product.objects.create(name="Product 1")
        url = reverse('product-detail', kwargs={'pk': product.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Product 1')

    # Test for updating a product by ID
    def test_update_product(self):
        product = Product.objects.create(name="Product 1")
        url = reverse('product-detail', kwargs={'pk': product.id})
        data = {'name': 'Updated Product'}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Product.objects.get().name, 'Updated Product')

    # Test for deleting a product by ID
    def test_delete_product(self):
        product = Product.objects.create(name="Product 1")
        url = reverse('product-detail', kwargs={'pk': product.id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Product.objects.count(), 0)
