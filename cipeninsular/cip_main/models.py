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
    
class Project(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField(blank=True, null=True)
    caratula = models.ImageField(upload_to='projects/thumbnails/')
    fecha_creado = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Proyecto"
        verbose_name_plural = "Proyectos"
    def __str__(self):
        return self.nombre

class ProjectImage(models.Model):
    proyecto = models.ForeignKey(Project, related_name='images', on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='projects/images/')
    caption = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        verbose_name = "Imagen del proyecto"
        verbose_name_plural = "Imágenes del proyecto"
    def __str__(self):
        return f"{self.proyecto.nombre} - Image"