from django.contrib import admin
from .models import Servicio, Slide, Project, ProjectImage

# Register your models here.
admin.site.register(Servicio)

class SlideAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'orden', 'estatus', 'imagen')
    list_editable = ('orden', 'estatus')
    search_fields = ('titulo',)
    ordering = ['orden']

admin.site.register(Slide, SlideAdmin)

class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 1  # Número de campos adicionales para agregar imágenes

class ProjectAdmin(admin.ModelAdmin):
    inlines = [ProjectImageInline]
    list_display = ('nombre', 'fecha_creado')

admin.site.register(Project, ProjectAdmin)