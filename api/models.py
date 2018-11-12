from django.db import models
from django.utils import timezone


class Anfitrion (models.Model):
    nombre = models.CharField(max_length=50)
    telefono = models.BigIntegerField
    domicilio = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Anfitriones"

    def __str__(self):
        return self.nombre


class Ciudad (models.Model):
    nombre = models.CharField(max_length=30)
    
    class Meta:
        verbose_name_plural = "Ciudades"

    def __str__(self):
        return self.nombre

class Propiedad (models.Model):
    title = models.CharField(max_length=25, default=None)
    descripcion = models.TextField(max_length=200)
    propietario = models.ForeignKey(Anfitrion,on_delete=models.CASCADE, default=None)
    imagen = models.ImageField(upload_to='images', max_length=100, null=True)
    tarifaDiaria = models.IntegerField()
    ciudad = models.ForeignKey(Ciudad,on_delete=models.CASCADE, null=True, blank=True, default=None)

    class Meta:
        verbose_name_plural = "Propiedades"

    def __str__(self):
        return self.title

class Reserva (models.Model):
    fechaRealizada = models.DateField(default =timezone.now)
    numeroReserva = models.AutoField(primary_key=True)
    propiedad = models.ForeignKey(Propiedad,on_delete=models.CASCADE, default=None)
    total = models.IntegerField(blank=True, null=True)

    def __str__ (self):
        return 'Reserva '+`self.numeroReserva`

class FechaAlq (models.Model):
    fecha = models.DateField(null=False)
    propiedad = models.ForeignKey(Propiedad, null=True, blank=True, on_delete=models.CASCADE, default= None)
    reserva = models.ForeignKey(Reserva, on_delete=models.PROTECT, blank=True, null=True, default = None)

    class Meta:
        verbose_name_plural = "FechasAlquiler"

    def __str__ (self):
        return 'Fecha N '+`self.id`

