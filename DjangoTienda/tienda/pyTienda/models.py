from django.db import models

# Create your models here.
#user: mauro
# pass: tiendamab90


class Productos(models.Model):
    nombre = models.CharField(max_length=120)
    descripcion = models.TextField(blank=True, null=True)
    precio = models.DecimalField(decimal_places=2, max_digits=10000)
    marca = models.CharField(max_length=100)
    numero = models.CharField(max_length=50)
