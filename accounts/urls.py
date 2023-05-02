from django.urls import path
from .views import VistaRegistro, VistaEditarPerfil, VistaCambiarPassword
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('registrarse/', VistaRegistro.as_view(), name = "registrarse"),
    path('editar_perfil/', VistaEditarPerfil.as_view(), name = "editar"),
    path('password/', VistaCambiarPassword.as_view(), name = "password"),
]