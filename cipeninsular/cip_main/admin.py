from django.contrib import admin
from .models import Servicio, Slide, Project, ProjectImage, Category, Producto, Empleado

# Register your models here.
@admin.register(Servicio)
class ServicioAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'descripcion')
    search_fields = ('titulo',)

class SlideAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'orden', 'estatus', 'imagen')
    list_editable = ('orden', 'estatus')
    search_fields = ('titulo',)
    ordering = ['orden']
    
    def vista_previa(self, obj):
        if obj.imagen:
            return f'<img src="{obj.imagen.url}" style="width: 50px; height: auto;" />'
        return "No Image"
    vista_previa.allow_tags = True
    vista_previa.short_description = "Vista Previa"

admin.site.register(Slide, SlideAdmin)

class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 1  # Número de campos adicionales para agregar imágenes
    fields = ('imagen', 'caption')

class ProjectAdmin(admin.ModelAdmin):
    inlines = [ProjectImageInline]
    list_display = ('nombre', 'fecha_creado', 'producto_asociado')
    list_filter = ('fecha_creado', 'categorias')
    search_fields = ('nombre',)
    filter_horizontal = ('categorias',)
    
    def listar_categorias(self, obj):
        return ", ".join([categoria.nombre for categoria in obj.categorias.all()])
    listar_categorias.short_description = "Categorías"

    def producto_info(self, obj):
        # Muestra el nombre del producto asociado en la lista de administración
        return obj.producto_asociado.nombre if obj.producto_asociado else "Sin producto asociado"
    producto_info.short_description = "Producto Asociado"
    
admin.site.register(Project, ProjectAdmin)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion')
    
@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'stock', 'destacado')
    list_filter = ('destacado',)
    search_fields = ('nombre',)
    actions = ['marcar_como_destacado']

    def marcar_como_destacado(self, request, queryset):
        queryset.update(destacado=True)
    marcar_como_destacado.short_description = "Marcar productos seleccionados como destacados"
    
@admin.register(Empleado)
class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'posicion')