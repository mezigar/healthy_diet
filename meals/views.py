from meals.models import Product, Meal
from meals.serializers import ProductSerializer, MealSerializer

from rest_framework.viewsets import ModelViewSet

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class MealViewSet(ModelViewSet):
    queryset = Meal.objects.all().order_by('-created')
    serializer_class = MealSerializer