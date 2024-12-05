from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_view, name='inicio'),  # Ruta raíz que muestra tu HTML
    path('chukum/', views.chukum_view, name='chukum'),
    path('servicios/', views.services_view, name='servicios'),
]
