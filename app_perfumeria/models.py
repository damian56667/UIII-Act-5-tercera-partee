from django.db import models

class Empleado(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField(blank=True, null=True)
    puesto = models.CharField(max_length=100, blank=True, null=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    fecha_contratacion = models.DateField(blank=True, null=True)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class Producto(models.Model):
    nombre = models.CharField(max_length=150, unique=True)
    descripcion = models.TextField(blank=True, null=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    stock = models.PositiveIntegerField(default=0)
    categoria = models.CharField(max_length=100, blank=True, null=True)
    fecha_creacion = models.DateField(auto_now_add=True)
    activo = models.BooleanField(default=True)
    sku = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.nombre


class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    direccion = models.CharField(max_length=250, blank=True, null=True)
    ciudad = models.CharField(max_length=100, blank=True, null=True)

    empleado = models.ForeignKey('Empleado', on_delete=models.SET_NULL, blank=True, null=True, related_name='clientes')

    # 🧠 CAMBIO A MUCHOS A MUCHOS (M:M)
    productos = models.ManyToManyField('Producto', related_name='clientes', blank=True)

    fecha_registro = models.DateField(auto_now_add=True)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
