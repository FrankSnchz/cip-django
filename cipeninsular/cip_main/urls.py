from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index_view, name='inicio'),  # Ruta raíz que muestra tu HTML
    path('chukum/', views.chukum_view, name='chukum'),
    path('servicios/', views.services_view, name='servicios'),
    path('serviciosgenerales/', views.generalservices_view, name='servicios generales'),
    path('__reload__/', include('django_browser_reload.urls')),  # Añade esta línea

]
