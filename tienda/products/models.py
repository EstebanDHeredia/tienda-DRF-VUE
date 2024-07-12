from django.db import models

# Create your models here.

# Modelo de productos
class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name="Nombre")
    description = models.TextField(verbose_name="Descripción")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Precio")


    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"
        ordering = ["name"]

    def __str__(self):
        return self.name