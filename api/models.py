from django.db import models
from django.utils import timezone


class Anfitrion (models.Model):
    nombre = models.CharField(max_length=50)
    telefono = models.BigIntegerField
    domicilio = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class Ciudad (models.Model):
    nombre = models.CharField(max_length=30)

    def __str__(self):
        return self.nombre


class Propiedad (models.Model):
    title = models.CharField(max_length=25, default=None)
    descripcion = models.TextField(max_length=200)
    propietario = models.ForeignKey(Anfitrion,on_delete=models.CASCADE, default=None)
    imagen = models.ImageField
    tarifaDiaria = models.IntegerField
    ciudad = models.ForeignKey(Ciudad,on_delete=models.CASCADE, default=None)


class Reserva (models.Model):
    fechaDeReserva = models.DateField(default = timezone.now)
    numeroReserva = models.IntegerField
    propiedad = models.ForeignKey(Propiedad,on_delete=models.CASCADE, default=None)


class FechaAlq (models.Model):
    fecha = models.DateField
    propiedad = models.ForeignKey(Propiedad,on_delete=models.CASCADE, default= None)
    reserva = models.ForeignKey(Reserva,on_delete=models.CASCADE, default = None)
