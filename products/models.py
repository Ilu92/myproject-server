from django.db import models

# Create your models here. модели = таблицы
# Был создан класс для таблицы
class ProductCategory(models.Model):
    name = models.CharField(max_length = 64, unique = True)
    description = models.TextField(blank=True)


class Product(models.Model):
    name = models.CharField(max_length=256)
    image = models.ImageField(upload_to='products_images', blank=True)
    description = models.CharField(max_length=64, blank=True, null=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.PositiveIntegerField(default=0)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
