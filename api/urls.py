from django.conf.urls import url
from views import *
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^$',first_view, name='api')
]

