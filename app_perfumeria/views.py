from django.shortcuts import render, redirect, get_object_or_404
from .models import Empleado, Producto, Cliente
import datetime

# -----------------------
# PÁGINA DE INICIO
# -----------------------
def inicio_perfumeria(request):
    context = {'now': datetime.datetime.now()}
    return render(request, 'inicio.html', context)


# ====================================================
# CRUD: EMPLEADO
# ====================================================
def ver_empleado(request):
    empleados = Empleado.objects.all().order_by('id')
    return render(request, 'empleado/ver_empleado.html', {'empleados': empleados})

def agregar_empleado(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        fecha_nacimiento = request.POST.get('fecha_nacimiento') or None
        puesto = request.POST.get('puesto')
        telefono = request.POST.get('telefono')
        email = request.POST.get('email')
        fecha_contratacion = request.POST.get('fecha_contratacion') or None

        Empleado.objects.create(
            nombre=nombre,
            apellido=apellido,
            fecha_nacimiento=fecha_nacimiento,
            puesto=puesto,
            telefono=telefono,
            email=email,
            fecha_contratacion=fecha_contratacion,
            activo=True
        )
        return redirect('ver_empleado')
    return render(request, 'empleado/agregar_empleado.html')

def actualizar_empleado(request, empleado_id):
    empleado = get_object_or_404(Empleado, id=empleado_id)
    return render(request, 'empleado/actualizar_empleado.html', {'empleado': empleado})

def realizar_actualizacion_empleado(request, empleado_id):
    empleado = get_object_or_404(Empleado, id=empleado_id)
    if request.method == 'POST':
        empleado.nombre = request.POST.get('nombre')
        empleado.apellido = request.POST.get('apellido')
        empleado.fecha_nacimiento = request.POST.get('fecha_nacimiento') or None
        empleado.puesto = request.POST.get('puesto')
        empleado.telefono = request.POST.get('telefono')
        empleado.email = request.POST.get('email')
        empleado.fecha_contratacion = request.POST.get('fecha_contratacion') or None
        activo_val = request.POST.get('activo')
        empleado.activo = True if activo_val == 'on' else False
        empleado.save()
        return redirect('ver_empleado')
    return redirect('actualizar_empleado', empleado_id=empleado.id)

def borrar_empleado(request, empleado_id):
    empleado = get_object_or_404(Empleado, id=empleado_id)
    if request.method == 'POST':
        empleado.delete()
        return redirect('ver_empleado')
    return render(request, 'empleado/borrar_empleado.html', {'empleado': empleado})


# ====================================================
# CRUD: PRODUCTO
# ====================================================
def ver_producto(request):
    productos = Producto.objects.all().order_by('id')
    return render(request, 'producto/ver_producto.html', {'productos': productos})

def agregar_producto(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        descripcion = request.POST.get('descripcion')
        precio = request.POST.get('precio') or 0.00
        stock = request.POST.get('stock') or 0
        categoria = request.POST.get('categoria')
        sku = request.POST.get('sku')

        Producto.objects.create(
            nombre=nombre,
            descripcion=descripcion,
            precio=precio,
            stock=stock,
            categoria=categoria,
            sku=sku,
            activo=True
        )
        return redirect('ver_producto')
    return render(request, 'producto/agregar_producto.html')

def actualizar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    return render(request, 'producto/actualizar_producto.html', {'producto': producto})

def realizar_actualizacion_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    if request.method == 'POST':
        producto.nombre = request.POST.get('nombre')
        producto.descripcion = request.POST.get('descripcion')
        producto.precio = request.POST.get('precio') or producto.precio
        producto.stock = request.POST.get('stock') or producto.stock
        producto.categoria = request.POST.get('categoria')
        producto.sku = request.POST.get('sku')
        activo_val = request.POST.get('activo')
        producto.activo = True if activo_val == 'on' else False
        producto.save()
        return redirect('ver_producto')
    return redirect('actualizar_producto', producto_id=producto.id)

def borrar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    if request.method == 'POST':
        producto.delete()
        return redirect('ver_producto')
    return render(request, 'producto/borrar_producto.html', {'producto': producto})


# ====================================================
# CRUD: CLIENTE (M:M con PRODUCTOS)
# ====================================================
def ver_cliente(request):
    clientes = Cliente.objects.all().order_by('id')
    return render(request, 'cliente/ver_cliente.html', {'clientes': clientes})

def agregar_cliente(request):
    empleados = Empleado.objects.filter(activo=True).order_by('nombre')
    productos = Producto.objects.filter(activo=True).order_by('nombre')

    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        telefono = request.POST.get('telefono')
        email = request.POST.get('email')
        direccion = request.POST.get('direccion')
        ciudad = request.POST.get('ciudad')
        empleado_id = request.POST.get('empleado')
        productos_ids = request.POST.getlist('productos')

        cliente = Cliente.objects.create(
            nombre=nombre,
            apellido=apellido,
            telefono=telefono,
            email=email,
            direccion=direccion,
            ciudad=ciudad,
            activo=True
        )

        if empleado_id:
            try:
                cliente.empleado = Empleado.objects.get(id=int(empleado_id))
            except Empleado.DoesNotExist:
                cliente.empleado = None
        cliente.save()

        if productos_ids:
            for pid in productos_ids:
                try:
                    producto = Producto.objects.get(id=int(pid))
                    cliente.productos.add(producto)
                except Producto.DoesNotExist:
                    pass

        return redirect('ver_cliente')

    return render(request, 'cliente/agregar_cliente.html', {'empleados': empleados, 'productos': productos})

def actualizar_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, id=cliente_id)
    empleados = Empleado.objects.filter(activo=True)
    productos = Producto.objects.filter(activo=True)

    if request.method == 'POST':
        cliente.nombre = request.POST.get('nombre')
        cliente.apellido = request.POST.get('apellido')
        cliente.telefono = request.POST.get('telefono')
        cliente.email = request.POST.get('email')
        cliente.direccion = request.POST.get('direccion')
        cliente.ciudad = request.POST.get('ciudad')
        empleado_id = request.POST.get('empleado')
        productos_ids = request.POST.getlist('productos')

        if empleado_id:
            try:
                cliente.empleado = Empleado.objects.get(id=int(empleado_id))
            except Empleado.DoesNotExist:
                cliente.empleado = None

        cliente.productos.clear()
        for pid in productos_ids:
            try:
                cliente.productos.add(Producto.objects.get(id=int(pid)))
            except Producto.DoesNotExist:
                pass

        cliente.save()
        return redirect('ver_cliente')

    return render(request, 'cliente/actualizar_cliente.html', {
        'cliente': cliente,
        'empleados': empleados,
        'productos': productos
    })

def realizar_actualizacion_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, id=cliente_id)
    if request.method == 'POST':
        cliente.nombre = request.POST.get('nombre')
        cliente.apellido = request.POST.get('apellido')
        cliente.email = request.POST.get('email')
        cliente.telefono = request.POST.get('telefono')
        cliente.direccion = request.POST.get('direccion')
        cliente.ciudad = request.POST.get('ciudad')
        cliente.save()
        return redirect('ver_cliente')
    return render(request, 'cliente/actualizar_cliente.html', {'cliente': cliente})

def borrar_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, id=cliente_id)
    if request.method == 'POST':
        cliente.delete()
        return redirect('ver_cliente')
    return render(request, 'cliente/borrar_cliente.html', {'cliente': cliente})
