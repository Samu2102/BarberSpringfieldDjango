from django.db import models

class Cita(models.Model):
    ESTADOS = [
        ('Pendiente', 'Pendiente'),
        ('Confirmada', 'Confirmada'),
        ('Cancelada', 'Cancelada'),
    ]

    cliente  = models.CharField(max_length=100)
    servicio = models.CharField(max_length=100)
    fecha    = models.DateField()
    hora     = models.CharField(max_length=20)
    barbero  = models.CharField(max_length=100)
    estado   = models.CharField(max_length=20, choices=ESTADOS, default='Pendiente')

    def __str__(self):
        return f"{self.cliente} - {self.servicio} - {self.fecha}"