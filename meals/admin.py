from django.contrib import admin
from meals.models import Meal, Product


admin.site.register(Product)
admin.site.register(Meal)
