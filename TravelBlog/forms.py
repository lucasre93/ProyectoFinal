from django import forms
from .models import Post, Categoria


paises = Categoria.objects.all().values_list('nombre','nombre')
lista_paises = []

for item in paises:
    lista_paises.append(item)

class FormularioPost(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('titulo', 'autor', 'categorias', 'cuerpo', 'imagen')
        widgets = {
            'titulo': forms.TextInput(attrs={'class':'form-control'}),
            'autor': forms.TextInput(attrs={'class':'form-control','value':'','id':'usuario','type':'hidden'}),
            'categorias': forms.Select(choices=lista_paises, attrs={'class':'form-control'}),
            'cuerpo': forms.Textarea(attrs={'class':'form-control'}),
        }

class FormularioEditarPost(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('titulo','autor','categorias','cuerpo')
        widgets = {
            'titulo': forms.TextInput(attrs={'class':'form-control'}),
            'autor': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id': 'usuario', 'type': 'hidden'}),
            'categorias': forms.Select(choices=lista_paises, attrs={'class':'form-control'}),
            'cuerpo': forms.Textarea(attrs={'class':'form-control'}),

        }