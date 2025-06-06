from django.urls import path
from . import views
from .views import (index, acercade, carrocompras, cuenta, gama_alta, gama_media, gama_baja, torrega1, torrega2,
                    torrega3, torrega4, torregb1, torregb2, torregb3, torregb4, torregm1, torregm2, torregm3, torregm4,
                    register, login_view, user_logout, perfil, agregarProducto, listaProductos, 
                    agregar_al_carrito, ver_carrito, eliminar_del_carrito, procesar_pago, paypal_return, paypal_cancel, 
                    modificarProducto, eliminarProducto, thank_you, descargar_boleta,borrar_historial, eliminar_usuario)

urlpatterns = [
    path('', index, name="index"),
    path('acercade/', acercade, name='acercade'),
    path('carrocompras/', carrocompras, name='carrocompras'),
    path('cuenta/', cuenta, name='cuenta'),
    path('GamaAlta/', gama_alta, name='GamaAlta'),
    path('buscar-productos/', views.buscar_productos, name='buscar_productos'),





    path('perfil/eliminar_usuario/', eliminar_usuario, name='eliminar_usuario'),

    path('GamaMedia/', gama_media, name='GamaMedia'),
    path('GamaBaja/', gama_baja, name='GamaBaja'),
    path('torrega1/', torrega1, name='torrega1'),
    path('torrega2/', torrega2, name='torrega2'),
    path('torrega3/', torrega3, name='torrega3'),
    path('torrega4/', torrega4, name='torrega4'),
    path('torregb1/', torregb1, name='torregb1'),
    path('torregb2/', torregb2, name='torregb2'),
    path('torregb3/', torregb3, name='torregb3'),
    path('torregb4/', torregb4, name='torregb4'),
    path('torregm1/', torregm1, name='torregm1'),
    path('torregm2/', torregm2, name='torregm2'),
    path('torregm3/', torregm3, name='torregm3'),
    path('torregm4/', torregm4, name='torregm4'),
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', user_logout, name='logout'),
    path('perfil/', perfil, name='perfil'),
    path('agregarProducto/', agregarProducto, name='agregarProducto'),
    path('listaProductos/', listaProductos, name='listaProductos'),
    path('agregar/<int:producto_id>/', agregar_al_carrito, name='agregar_al_carrito'),
    path('carrito/', ver_carrito, name='ver_carrito'),
    path('eliminar/<int:item_id>/', eliminar_del_carrito, name='eliminar_del_carrito'),
    path('paypal/procesar/', procesar_pago, name='procesar_pago'),
    path('paypal/return/', paypal_return, name='paypal_return'),
    path('paypal/cancel/', paypal_cancel, name='paypal_cancel'),
    path('modificar/', modificarProducto, name='modificar_producto'),
    path('eliminarProducto/', eliminarProducto, name='eliminar_producto'),
    path('thank_you/', thank_you, name='thank_you'),
    path('descargar_boleta/', descargar_boleta, name='descargar_boleta'),
    path('borrar_historial/', borrar_historial, name='borrar_historial'),
    path('perfil/borrar_compra/<int:compra_id>/', views.borrar_compra_individual, name='borrar_compra_individual'),
    path('perfil/borrar_compra/<int:compra_id>/', views.borrar_compra_individual, name='borrar_compra_individual'),    
]
