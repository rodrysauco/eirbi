# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import (FechaAlq, Propiedad, Anfitrion, Ciudad, Reserva)

# Register your models here.
admin.site.register(FechaAlq)
admin.site.register(Propiedad)
admin.site.register(Anfitrion)
admin.site.register(Ciudad)
admin.site.register(Reserva)

