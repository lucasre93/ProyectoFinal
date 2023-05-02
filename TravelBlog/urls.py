from django.urls import path, include
from . import views
from .views import VistaHome, VistaArticulo, AgregarPost, EditarPost, EliminarPost, AgregarCategoria, VistaCategoria, AboutMe
urlpatterns = [
    path('', VistaHome.as_view(), name = "home"),
    path('articulo/<int:pk>', VistaArticulo.as_view(), name = "articulodetalle"),
    path('agregar_post/', AgregarPost.as_view(), name = "agregarpost"),
    path('articulo/editar/<int:pk>', EditarPost.as_view(), name = "editarpost"),
    path('articulo/eliminar/<int:pk>', EliminarPost.as_view(), name = "eliminarpost"),
    path('agregar_categoria/', AgregarCategoria.as_view(), name = "agregarcategoria"),
    path('categorias/<str:categ>/', VistaCategoria, name = "categorias"),
    path('aboutme/', AboutMe, name = "aboutme"),

]