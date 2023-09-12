from django.db import models

class Product(models.Model):
    brand = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    amount = models.IntegerField()
    description = models.TextField()
    price = models.TextField()