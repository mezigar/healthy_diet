from meals.models import Product, Meal
from meals.serializers import ProductSerializer, MealSerializer

from rest_framework import generics

class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class MealList(generics.ListCreateAPIView):
    queryset = Meal.objects.all().order_by('-created')
    serializer_class = MealSerializer