from django.db import models

class Cita(models.Model):

    cliente = models.CharField(max_length=100)

    servicio = models.CharField(max_length=100)

    hora = models.CharField(max_length=20)

    estado = models.CharField(
        max_length=20,
        default='Pendiente'
    )

    def __str__(self):
        return self.cliente
