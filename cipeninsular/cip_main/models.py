from django.db import models

# Create your models here.
class Servicio(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='servicios/')
    
    def __str__(self):
        return self.titulo
    
class Slide(models.Model):
    titulo = models.CharField(max_length=255, verbose_name="Título")
    imagen = models.ImageField(upload_to='slides/', verbose_name="Imagen")
    descripcion = models.TextField(blank=True, null=True, verbose_name="Descripción")
    orden = models.PositiveIntegerField(default=1, verbose_name="Orden")
    estatus = models.BooleanField(default=True, verbose_name="Activo")

    class Meta:
        ordering = ['orden']

    def __str__(self):
        return self.titulo
    
class Category(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"

    def __str__(self):
        return self.nombre
    
class Producto(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre del Producto")
    descripcion = models.TextField(verbose_name="Descripción")
    precio = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Precio")
    imagen_caratula = models.ImageField(upload_to='imagenes_productos/', verbose_name="Imagen de Carátula")
    stock = models.PositiveIntegerField(default=0, verbose_name="Stock Disponible")
    destacado = models.BooleanField(default=False, verbose_name="Producto Destacado")

    def __str__(self):
        return self.nombre

class Project(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField(blank=True, null=True)
    caratula = models.ImageField(upload_to='projects/thumbnails/')
    fecha_creado = models.DateTimeField(auto_now_add=True)
    categorias = models.ManyToManyField(Category, related_name='proyectos', blank=True)
    producto_asociado = models.ForeignKey(
        Producto, 
        related_name='proyectos', 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True,
        verbose_name="Producto asociado"
    )

    class Meta:
        verbose_name = "Proyecto"
        verbose_name_plural = "Proyectos"

    def __str__(self):
        return self.nombre

class ProjectImage(models.Model):
    proyecto = models.ForeignKey(
        Project, 
        related_name='images', 
        on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='projects/images/')
    caption = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        verbose_name = "Imagen del proyecto"
        verbose_name_plural = "Imágenes del proyecto"

    def __str__(self):
        # Si hay un producto asociado, mostramos el nombre del producto
        producto_info = f" - Producto: {self.proyecto.producto_asociado.nombre}" if self.proyecto.producto_asociado else " - Sin producto asociado"
        return f"{self.proyecto.nombre}{producto_info}"