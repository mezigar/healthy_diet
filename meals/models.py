from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=50)
    proteins = models.DecimalField(max_digits=5, decimal_places=2)
    carbs = models.DecimalField(max_digits=5, decimal_places=2)
    fats = models.DecimalField(max_digits=5, decimal_places=2)
    calories = models.IntegerField()
    image = models.ImageField(upload_to='products/')

    def __str__(self):
        return f'<{self.id}> {self.title}' 


class Meal(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    products = models.ManyToManyField(Product)
    total_proteins = models.DecimalField(max_digits=5, decimal_places=2)
    total_carbs = models.DecimalField(max_digits=5, decimal_places=2)
    total_fats = models.DecimalField(max_digits=5, decimal_places=2)
    total_calories = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='meals/')

    class Meta:
        ordering = ['created']

    def __str__(self):
        return f'<{self.id}> {self.title}'