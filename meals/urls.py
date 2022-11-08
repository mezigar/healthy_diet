from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from meals import views


urlpatterns = [
    path('', views.MealList.as_view()),
    path('products/', views.ProductList.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)