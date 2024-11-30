from django.shortcuts import render
from .models import Servicio, Slide, Project

# Create your views here.
def index(request):
    servicios = Servicio.objects.all()  # Obtienes todos los servicios
    slides = Slide.objects.filter(estatus=True).order_by('orden')  # Obtienes los slides activos y los ordenas
    proyectos = Project.objects.prefetch_related('images').all()

    return render(request, 'index.html', {'servicios': servicios, 'slides': slides, 'proyectos': proyectos})