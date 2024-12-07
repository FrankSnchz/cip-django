from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index_view, name='inicio'),  # Ruta raíz que muestra tu HTML
    path('chukum/', views.chukum_view, name='chukum'),
    path('servicios/', views.services_view, name='servicios'),
    path('servicios-detallados/', views.detailed_services_view, name='servicios detallados'),
    path('contacto/', views.contact_us_view, name='contacto'),
    path('__reload__/', include('django_browser_reload.urls')),  # Añade esta línea

]
