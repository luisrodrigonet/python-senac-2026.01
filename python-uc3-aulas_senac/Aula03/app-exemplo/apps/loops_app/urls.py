from django.urls import path
from . import views

"""
No Django, o conceito de namespace (espaço de nomes) é amplamente utilizado para organizar recursos, 
evitar colisões de nomes entre diferentes aplicações e permitir a reutilização modular de código
"""
app_name = "loops" # Aula 03

urlpatterns = [
    path('', views.index, name='index'), # Aula 03
    path('for/', views.pagina_for, name='pagina_for'),
    path('jogo/', views.jogo_adivinhacao, name='jogo_adivinhacao'),
    path('amortizacao/', views.amortizacao_divida, name='amortizacao'),
    path('fatores/', views.fatores_primos, name='fatores'),
]