from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio_perfumeria, name='inicio_perfumeria'),

    # Empleado (ya existentes)
    path('empleado/', views.ver_empleado, name='ver_empleado'),
    path('empleado/agregar/', views.agregar_empleado, name='agregar_empleado'),
    path('empleado/actualizar/<int:empleado_id>/', views.actualizar_empleado, name='actualizar_empleado'),
    path('empleado/actualizar/realizar/<int:empleado_id>/', views.realizar_actualizacion_empleado, name='realizar_actualizacion_empleado'),
    path('empleado/borrar/<int:empleado_id>/', views.borrar_empleado, name='borrar_empleado'),

    # Producto (ya existentes)
    path('producto/', views.ver_producto, name='ver_producto'),
    path('producto/agregar/', views.agregar_producto, name='agregar_producto'),
    path('producto/actualizar/<int:producto_id>/', views.actualizar_producto, name='actualizar_producto'),
    path('producto/actualizar/realizar/<int:producto_id>/', views.realizar_actualizacion_producto, name='realizar_actualizacion_producto'),
    path('producto/borrar/<int:producto_id>/', views.borrar_producto, name='borrar_producto'),

    # Cliente (nuevo)
    path('cliente/', views.ver_cliente, name='ver_cliente'),
    path('cliente/agregar/', views.agregar_cliente, name='agregar_cliente'),
    path('cliente/actualizar/<int:cliente_id>/', views.actualizar_cliente, name='actualizar_cliente'),
    path('cliente/actualizar/realizar/<int:cliente_id>/', views.realizar_actualizacion_cliente, name='realizar_actualizacion_cliente'),
    path('cliente/borrar/<int:cliente_id>/', views.borrar_cliente, name='borrar_cliente'),
]
