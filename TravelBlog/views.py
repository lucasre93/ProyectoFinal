from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Categoria
from .forms import FormularioPost, FormularioEditarPost
from django.urls import reverse_lazy
# Create your views here.

class VistaHome(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-id']

    def get_context_data(self, *args, **kwargs):
        categ_menu = Categoria.objects.all()
        context = super(VistaHome, self).get_context_data(*args, *kwargs)
        context["categ_menu"] = categ_menu
        return context

class VistaArticulo(DetailView):
    model = Post
    template_name = 'articulo_detalles.html'

    def get_context_data(self, *args, **kwargs):
        categ_menu = Categoria.objects.all()
        context = super(VistaArticulo, self).get_context_data()
        context["categ_menu"] = categ_menu
        return context

class AgregarPost(CreateView):
    model = Post
    form_class = FormularioPost
    template_name = 'agregar_post.html'

    def get_context_data(self, *args, **kwargs):
        categ_menu = Categoria.objects.all()
        context = super(AgregarPost, self).get_context_data()
        context["categ_menu"] = categ_menu
        return context

class EditarPost(UpdateView):
    model = Post
    template_name = 'editar_post.html'
    form_class = FormularioEditarPost

    def get_context_data(self, *args, **kwargs):
        categ_menu = Categoria.objects.all()
        context = super(EditarPost, self).get_context_data(*args, **kwargs)
        context["categ_menu"] = categ_menu
        return context

class EliminarPost(DeleteView):
    model = Post
    template_name = 'eliminar_post.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *args, **kwargs):
        categ_menu = Categoria.objects.all()
        context = super(EliminarPost, self).get_context_data(*args,**kwargs)
        context["categ_menu"] = categ_menu
        return context

class AgregarCategoria(CreateView):
    model = Categoria
    template_name = 'agregar_categoria.html'
    fields = '__all__'

def VistaCategoria(request, categ):
    categorias_post = Post.objects.filter(categorias=categ)
    return render(request, 'categorias.html', {'categ':categ, 'categorias_post': categorias_post})

def AboutMe(request):
    return render(request, 'aboutme.html')