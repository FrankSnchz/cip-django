from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='inicio'),  # Ruta raíz que muestra tu HTML
]
