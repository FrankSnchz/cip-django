from django.shortcuts import render
from .models import Servicio, Slide, Project, Category, Producto, Empleado

# Create your views here.
def index_view(request):
    servicios = Servicio.objects.all()  # Obtienes todos los servicios
    slides = Slide.objects.filter(estatus=True).order_by('orden')  # Obtienes los slides activos y los ordenas
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


    # Obtener los slides activos ordenados
    slides = Slide.objects.filter(estatus=True).order_by('orden')

    return render(request, 'chukum.html', {
        'proyectos': proyectos_chukum,
        'productos': productos,
        'slides': slides,
        'productos-chukum': productos_chukum,
    })

def servicios_view(request):
    # Puedes añadir datos al contexto si es necesario.
    context = {
        'titulo': 'Nuestros Servicios',
        'descripcion': 'Descubre los servicios que ofrecemos.',
    }
    
    
    return render(request, 'services.html', {      
                  })