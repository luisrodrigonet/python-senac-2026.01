from django.urls import path
from . import views

app_name = 'agenda_json'

urlpatterns = [
    path('', views.agenda_listar, name='index'),
    path('listar/', views.agenda_listar, name='agenda_listar'),
    path('adicionar/', views.agenda_adicionar, name='agenda_adicionar'),
    path('<int:contato_id>/remover/', views.agenda_remover, name='agenda_remover'),
    path('<int:contato_id>/editar/', views.agenda_editar, name='agenda_editar'),
]