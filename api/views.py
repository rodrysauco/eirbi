# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import Http404
from api.models import *
from datetime import datetime
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
    except Propiedad.DoesNotExist:
        raise Http404("La propiedad ingresada no existe")
    return render(request, 'propiedad.html', {'property': prop, 'form': ReservaForm()})


def reservaPropiedad(request):
    if request.method == 'POST':
        diaInicio = datetime.strptime(
            request.POST['dateFrom'], '%Y-%m-%d').date()
        diaFin = datetime.strptime(request.POST['dateTo'], '%Y-%m-%d').date()
        propiedadAlquilar = Propiedad.objects.get(
            id=request.POST['propertyId'])
        fechasDeReserva = Reserva.objects.filter(
            propiedad=propiedadAlquilar.id)

        for fechaReserva in fechasDeReserva:
            if fechaReserva.fechaDeReservaInicio is not None and fechaReserva.fechaDeReservaFin is not None:
                
                Range = namedtuple('Range', ['start', 'end'])
                r1 = Range(start=fechaReserva.fechaDeReservaInicio, end=fechaReserva.fechaDeReservaFin)
                r2 = Range(start=diaInicio, end=diaFin)
                latest_start = max(r1.start, r2.start)
                earliest_end = min(r1.end, r2.end)
                delta = (earliest_end - latest_start).days + 1
                overlap = max(0, delta)
                
                if overlap > 0:
                    return render(request, 'sinDisponibilidad.html')

        r = Reserva(
            fechaDeReservaInicio=diaInicio,
            fechaDeReservaFin=diaFin,
            propiedad=propiedadAlquilar,
            total=request.POST['total'])
        r.save()
    
        return redirect('reservaExitosa', r.numeroReserva)
    return render(request, '404.html')


def reservaExitosa(request, idReserva):
    try:
        reserva = Reserva.objects.get(id=idReserva)
    except Propiedad.DoesNotExist:
        raise Http404("Propiedad no encontrada")
    return render(request, 'reservaExitosa.html', {'reserva': reserva})
