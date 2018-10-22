from django.db import models


class FechaAlq (models.Model):
    fecha = models.DateField


class Propiedad (models.Model):
    descripcion = models.TextField(max_length=200)
    imagen = models.ImageField
    tarifaDiaria = models.IntegerField
    fecha = models.ForeignKey(FechaAlq, on_delete=models.CASCADE)


class Anfitrion (models.Model):
    nombre = models.CharField(max_length=50)
    telefono = models.BigIntegerField
    domicilio = models.CharField(max_length=100)


class Ciudad (models.Model):
    nombre = models.CharField(max_length=30)


class Reserva (models.Model):
    fecha = models.ForeignKey(FechaAlq, on_delete=models.CASCADE)
