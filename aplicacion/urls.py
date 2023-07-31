from django.urls import path, include
from .views import *

urlpatterns = [
    path('', index, name="inicio"),

    path('alquileres/', alquileres, name="alquileres"),

    path('compras/', compras, name="compras"),

    path('ventas/', ventas, name="ventas"),

    path('equipos/', equipos, name="equipos"),

    path('equipo_form/', equipoForm, name="equipo_form"),

    path('equipo_form2/', equipoForm2, name="equipo_form2"),

    path('alquiler_form/', alquilerForm, name="alquiler_form"),

    path('alquiler_form2/', alquilerForm2, name="alquiler_form2"),

    path('buscar_precio/', buscarPrecio, name="buscar_precio"),

    path('buscar2/', buscar2, name="buscar2"),


]