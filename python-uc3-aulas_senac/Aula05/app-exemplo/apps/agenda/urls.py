##
# APP: agenda - urls.py
##
from django.urls import path
from . import views

"""
No Django, o conceito de namespace (espaço de nomes) é amplamente utilizado para organizar recursos, 
evitar colisões de nomes entre diferentes aplicações e permitir a reutilização modular de código
"""
app_name = "agenda" # Aula 05

urlpatterns = [
    path('', views.index, name='index'),
]