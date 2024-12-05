from django.shortcuts import render, get_object_or_404
from .models import Servicio, Slide, Project, Category, Producto, Empleado

# Create your views here.
def index_view(request):
    servicios = Servicio.objects.filter(parent__isnull=True)
    slides = Slide.objects.filter(estatus=True, servicio__isnull=True).order_by('orden')
    proyectos = Project.objects.prefetch_related('images').all()
    empleados = Empleado.objects.all()

    return render(request, 'index.html', {'servicios': servicios, 'slides': slides, 'proyectos': proyectos, 'empleados': empleados})

def chukum_view(request):
    productos = Producto.objects.all()  # Asegúrate de que esté obteniendo todos los productos
    
    # Obtener la categoría "Chukum"
    try:
        chukum_category = Category.objects.get(nombre="Chukum")
    except Category.DoesNotExist:
        # Si no existe la categoría, redirigir o mostrar un mensaje
        return render(request, '404.html', {'message': "Categoría Chukum no encontrada"})

    # Filtrar los proyectos que tienen la categoría "Chukum"
    proyectos_chukum = Project.objects.filter(categorias=chukum_category).prefetch_related('images')

    # Filtrar los productos destacados relacionados con los proyectos de Chukum
    productos_chukum = Producto.objects.filter(
        proyectos__in=proyectos_chukum,  # Usamos la relación inversa 'proyectos'
        destacado=True  # Solo productos destacados
    ).distinct().prefetch_related('proyectos__images')  # Prefetch de las imágenes de proyectos



    return render(request, 'chukum.html', {
        'proyectos': proyectos_chukum,
        'productos': productos,
        'productos-chukum': productos_chukum,
    })

def services_view(request):
    servicio_id = request.GET.get('servicio_id')  # Obtenemos el servicio_id desde la URL
    servicios = Servicio.objects.filter(parent__isnull=True)
    print(f"Servicios principales obtenidos: {servicios}")
    
    subservicio = None  # O algún valor predeterminado
    slides = []
    if servicio_id:
        subservicio = get_object_or_404(Servicio, id=servicio_id)
        print(f"Subservicio encontrado: {subservicio}")

        
        # Obtenemos las slides relacionadas con el servicio (subservicio o servicio principal)
        slides = Slide.objects.filter(servicio=subservicio)  # Filtramos por servicio
        print(f"Slides asociados al subservicio {subservicio.titulo}: {slides}")

        $$##FALTA AGREGAR COSAS
    
    return render(request, 'services.html', {
        'servicios':servicios, 
        'subservicio':subservicio, 
        'slides':slides
    })