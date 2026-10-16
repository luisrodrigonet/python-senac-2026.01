from django.urls import path
from . import views

urlpatterns = [
    path('for/', views.pagina_for, name='pagina_for'),
    path('para/',views.pagina_for, name='laco_for'),
]
