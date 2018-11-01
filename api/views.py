# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import Http404
from api.models import *
from datetime import datetime


# Create your views here.
def index(request):
    ciudades = Ciudad.objects.all()
    if 'filter' in request.GET:
        filtrados = Propiedad.objects.all().filter(
            ciudad=request.GET['idCiudad'])
        contexto = {
            'propiedades': filtrados,
            'ciudades': ciudades
        }
        return render(request, 'index.html', contexto)
    else:
        propiedades = Propiedad.objects.all()
        contexto = {
            'propiedades': propiedades,
            'ciudades': ciudades
        }
        return render(request, 'index.html', contexto)


def propiedad(request, propiedadid):
    try:
        prop = Propiedad.objects.get(id=propiedadid)
    except Propiedad.DoesNotExist:
        raise Http404("La propiedad ingresada no existe")
    return render(request, 'propiedad.html', {'propiedad': propiedad})


def reservaPropiedad(request):
    if request.method == 'POST':
        DiaInicio = datetime.strptime(
            request.POST['dateFrom'], '%Y-%m-%d').date()
        DiaFin = datetime.strptime(request.POST['dateTo'], '%Y-%m-%d').date()
        propiedadAlquilar = Propiedad.objects.get(
            id=request.POST['propertyId'])
        fechasDeReserva = Reserva.objects.filter(
            propiedad=propiedadAlquilar.id)
        for fechaReserva in fechasDeReserva:
            if fechaReserva.fechaReserva is not None:
                if DiaInicio <= fechaReserva.fechaReserva <= DiaFin:
                    return render(request, 'sinDisponibilidad.html')
        r = Reserva(
            fechaDeReserva=datetime.now().date(),
            propiedad=propiedadAlquilar,
            total=request.POST['total'])
        r.save()
        for fechaReserva in fechasDeReserva:
            if DiaInicio <= fechaReserva.fechaReserva <= DiaFin:
                fechaReserva.fechaReserva = r
                fechaReserva.save()
        r.total = propiedadAlquilar.tarifaDiaria * propiedadAlquilar.fechaAlquiler_set.filter(reserva=r).count()
        r.save()
        return redirect('reservaExitosa', r.numeroReserva)
    return render(request, 'reservaExitosa.html')


def reservaExitosa(request, idReserva):
    try:
        reserva = Reserva.objects.get(id=idReserva)
    except Propiedad.DoesNotExist:
        raise Http404("Propiedad no encontrada")
    return render(request, 'reservaExitosa.html', {'reserva': reserva})
