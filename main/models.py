from django.db import models


class Material(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    code = models.IntegerField(unique=True)

    def __str__(self):
        return self.name


class ProductMaterial(models.Model):
    product = models.ForeignKey(Product, models.CASCADE, related_name='materials')
    material = models.ForeignKey(Material, models.CASCADE)
    quantity = models.FloatField()

    def __str__(self):
        return self.product.name + " - " + self.material.name


class Warehouse(models.Model):
    material = models.ForeignKey(Material, models.CASCADE, related_name='warehouse')
    qty = models.IntegerField()
    price = models.IntegerField()

    def __str__(self):
        return self.material.name + " - " + str(self.qty) + " - " + str(self.price)
