# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import Http404
from api.models import *
from datetime import datetime
from django.utils import formats
from collections import namedtuple
from api.forms import ReservaForm

def render404(request):
    return render(request, '404.html', status=404)

# Create your views here.
def index(request):
    filtro = request.GET.get('filter')
    ciudades = Ciudad.objects.all()
    if filtro == 'true':
        filtrados = Propiedad.objects.all().filter(ciudad=request.GET['cities'])
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
        fechasDisp = FechaAlq.objects.filter(propiedad=prop,reserva = None)

    except Propiedad.DoesNotExist:
        raise Http404("La propiedad ingresada no existe")
    return render(request, 'propiedad.html', {'property': prop, 'form': ReservaForm(), 'fechasDisp': fechasDisp})


def reservaPropiedad(request):
    if request.method == 'POST':
        dates = dict(request.POST)['dates']

        print(dates)

        propiedadAlquilar = Propiedad.objects.get(
            id=request.POST['propertyId'])

        r = Reserva(
            propiedad=propiedadAlquilar,
            total=request.POST['total'])
        r.save()

        for date in dates:
            """ fecha = formats.date_format(date, "SHORT_DATETIME_FORMAT") """
            f = FechaAlq.objects.get(fecha=date, propiedad=propiedadAlquilar)
            f.reserva = r
            f.save(force_update=True)
    
        return redirect('apiAlq:reservaExitosa', r.numeroReserva)
    return render(request, '404.html')


def reservaExitosa(request, idReserva):
    try:
        reserva = Reserva.objects.get(numeroReserva=idReserva)
    except Propiedad.DoesNotExist:
        raise Http404("Propiedad no encontrada")
    return render(request, 'reservaExitosa.html', {'reserva': reserva})
