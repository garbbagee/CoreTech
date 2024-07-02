from django.urls import path
from . import views
from .views import index, acercade, carrocompras, cuenta, gama_alta, gama_media, gama_baja, torrega1, torrega2, torrega3, torrega4, torregb1, torregb2, torregb3, torregb4, torregm1, torregm2, torregm3, torregm4, register, login_view, agregarProducto, listaProductos
urlpatterns = [
  	path('',index,name="index"),
    path('acercade/', acercade, name='acercade'),
    path('carrocompras/', carrocompras, name='carrocompras'),
    path('cuenta/', cuenta, name='cuenta'),
    path('GamaAlta/', gama_alta, name='GamaAlta'),
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
    path('agregarProducto/', views.agregarProducto, name='agregarProducto'),
    path('listaProductos/', views.listaProductos, name='listaProductos'),
]