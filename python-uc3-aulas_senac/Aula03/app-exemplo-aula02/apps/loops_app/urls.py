from django.urls import path
from . import views

urlpatterns = [
    path('for/', views.pagina_for, name='pagina_for'),
    path('jogo/', views.jogo_adivinhacao, name='jogo_adivinhacao'),
]