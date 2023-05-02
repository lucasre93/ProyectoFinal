from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.urls import reverse_lazy
from .forms import FormularioRegistro, FormularioEditarPerfil
from django.contrib.auth.views import PasswordChangeView

class VistaRegistro(generic.CreateView):
    form_class = FormularioRegistro
    template_name = 'registration/registro.html'
    success_url = reverse_lazy('login')

class VistaEditarPerfil(generic.UpdateView):
    form_class = FormularioEditarPerfil
    template_name = 'registration/editar_perfil.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user

class VistaCambiarPassword(PasswordChangeView):
    form_class = PasswordChangeView
    success_url = reverse_lazy('home')