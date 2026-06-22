from django.db import models

class Cita(models.Model):
    ESTADOS = [
        ('Pendiente', 'Pendiente'),
        ('Confirmada', 'Confirmada'),
        ('Cancelada', 'Cancelada'),
    ]
    cliente     = models.CharField(max_length=100)
    servicio    = models.CharField(max_length=100)
    adicionales = models.CharField(max_length=200, blank=True, default='')
    productos   = models.CharField(max_length=200, blank=True, default='')
    fecha       = models.DateField()
    hora        = models.CharField(max_length=20)
    barbero     = models.CharField(max_length=100)
    estado      = models.CharField(max_length=20, choices=ESTADOS, default='Pendiente')
    def __str__(self):
        return f"{self.cliente} - {self.servicio} - {self.fecha}"
