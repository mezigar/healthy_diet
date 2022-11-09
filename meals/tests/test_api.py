from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework.status import HTTP_200_OK
from meals.models import Product
from meals.serializers import ProductSerializer

class MealsApiTestCase(APITestCase):
    def test_get_product(self):
        product1 = Product.objects.create(title='Chicken Breast',proteins=24.00,carbs=0.00,fats=3.00,calories=113) 
        product2 = Product.objects.create(title='tomatoes', proteins=0.90,carbs=3.90,fats=0.20, calories=18)
        url = reverse('product-list')
        response = self.client.get(url)
        self.assertEqual(HTTP_200_OK, response.status_code)
        self.assertEqual(ProductSerializer([product1, product2], many=True).data, response.data)

        url = reverse('product-detail', kwargs={'pk':1})
        response = self.client.get(url)
        self.assertEqual(HTTP_200_OK, response.status_code)
        self.assertEqual(ProductSerializer(product1).data, response.data)