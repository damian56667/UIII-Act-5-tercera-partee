from django.contrib import admin
from .models import Empleado, Producto, Cliente

@admin.register(Empleado)
class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'apellido', 'puesto', 'telefono', 'email', 'activo')
    search_fields = ('nombre', 'apellido', 'puesto')
    list_filter = ('activo',)

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'precio', 'stock', 'categoria', 'activo')
    search_fields = ('nombre', 'categoria')
    list_filter = ('activo', 'categoria')

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'apellido', 'telefono', 'email', 'mostrar_productos', 'mostrar_empleados', 'activo')
    search_fields = ('nombre', 'apellido', 'email')
    list_filter = ('activo',)

    # 🔹 Función para mostrar los productos relacionados
    def mostrar_productos(self, obj):
        return ", ".join([p.nombre for p in obj.productos.all()])
    mostrar_productos.short_description = "Productos"

    # 🔹 Función para mostrar los empleados relacionados
    def mostrar_empleados(self, obj):
        return ", ".join([e.nombre for e in obj.empleados.all()])
    mostrar_empleados.short_description = "Empleados"
