# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import (FechaAlq, Propiedad, Anfitrion, Ciudad,
                     Reserva)

# Register your models here.

class FechaAlquiler_Inline (admin.TabularInline):
    model = FechaAlq
    fk_name = "propiedad"
    extra = 0
    #exclude = ['reserva',]


class PropiedadAdmin (admin.ModelAdmin):
    inlines = [FechaAlquiler_Inline, ]

#Models registered in the site
admin.site.register(FechaAlq)
admin.site.register(Propiedad, PropiedadAdmin)
admin.site.register(Anfitrion)
admin.site.register(Ciudad)
admin.site.register(Reserva)