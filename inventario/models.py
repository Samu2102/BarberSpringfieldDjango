from django.db import models
from citas.models import Servicio

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.IntegerField()
    stock  = models.IntegerField()

    def __str__(self):
        return self.nombre

    @property
    def estado(self):
        if self.stock >= 10:
            return 'Suficiente'
        elif self.stock >= 6:
            return 'Medio'
        else:
            return 'Bajo'

class ServicioProducto(models.Model):
    servicio  = models.ForeignKey(Servicio, on_delete=models.CASCADE, related_name='productos_usados')
    producto  = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad  = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.servicio.nombre} → {self.producto.nombre} x{self.cantidad}"