from rest_framework import status
from rest_framework.test import APITestCase
from .models import Product

class ProductTests(APITestCase):

    def setUp(self):
        self.product = Product.objects.create(name="Sample Product")

    # Test updating a product by name
    def test_update_product_by_name(self):
        url = '/api/products/update/name/?name=Sample Product'
        data = {'name': 'Updated Product'}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.product.refresh_from_db()
        self.assertEqual(self.product.name, 'Updated Product')

    # Test deleting a product by name
    def test_delete_product_by_name(self):
        url = '/api/products/delete/name/?name=Sample Product'
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        with self.assertRaises(Product.DoesNotExist):
            Product.objects.get(name="Sample Product")

    # Test updating a product by ID
    def test_update_product(self):
        url = f'/api/products/update/id/{self.product.pk}/'
        data = {'name': 'Updated Sample Product'}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.product.refresh_from_db()
        self.assertEqual(self.product.name, 'Updated Sample Product')

    # Test deleting a product by ID
    def test_delete_product(self):
        url = f'/api/products/delete/id/{self.product.pk}/'  # Update the URL
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        with self.assertRaises(Product.DoesNotExist):
            Product.objects.get(pk=self.product.pk)
