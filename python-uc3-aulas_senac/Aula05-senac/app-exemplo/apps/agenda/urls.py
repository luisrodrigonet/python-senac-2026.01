##
# APP: loops_app - urls.py
##
from django.urls import path
from . import views

"""
No Django, o conceito de namespace (espaço de nomes) é amplamente utilizado para organizar recursos, 
evitar colisões de nomes entre diferentes aplicações e permitir a reutilização modular de código
"""
app_name = "agenda" # Aula 05

urlpatterns = [
    path('', views.agenda_listar, name='index'), # Aula 05
    path('listar/', views.agenda_listar, name='agenda_listar'),
    path('adicionar/', views.agenda_adicionar, name='agenda_adicionar'),
    path('<int:contato_id>/remover/', views.agenda_remover, name='agenda_remover'),
    path('<int:contato_id>/editar/', views.agenda_editar, name='agenda_editar'),
]