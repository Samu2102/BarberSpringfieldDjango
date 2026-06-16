from django.db import models

class Barbero(models.Model):
    nombre      = models.CharField(max_length=100)
    cedula      = models.CharField(max_length=20, unique=True)
    especialidad = models.CharField(max_length=100)
    telefono    = models.CharField(max_length=20)
    email       = models.EmailField(unique=True)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    ESTADOS = [
        ('Suficiente', 'Suficiente'),
        ('Medio', 'Medio'),
        ('Bajo', 'Bajo'),
    ]
    nombre = models.CharField(max_length=100)
    precio = models.IntegerField()
    stock  = models.IntegerField()
    estado = models.CharField(max_length=20, choices=ESTADOS, default='Suficiente')

    def __str__(self):
        return self.nombre

class Servicio(models.Model):
    nombre      = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio      = models.IntegerField()
    duracion    = models.IntegerField(help_text="Duración en minutos")

    def __str__(self):
        return self.nombre

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