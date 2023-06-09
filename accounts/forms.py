from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django import forms

class FormularioRegistro(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    first_name = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta:
        model = User
        fields = ('username','first_name','last_name','email', 'password1','password2')

    def __init__(self, *args, **kwargs):
        super(FormularioRegistro, self).__init__(*args,**kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'


class FormularioEditarPerfil(UserChangeForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    first_name = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class':'form-control'}))
    username = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class':'form-control'}))
    last_login = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','type':'hidden'}))
    is_superuser = forms.CharField(max_length=30, widget=forms.CheckboxInput(attrs={'class':'form-check','type':'hidden'}))
    is_staff = forms.CharField(max_length=30, widget=forms.CheckboxInput(attrs={'class':'form-check','type':'hidden'}))
    is_active = forms.CharField(max_length=30, widget=forms.CheckboxInput(attrs={'class':'form-check','type':'hidden'}))
    date_joined = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','type':'hidden'}))

    class Meta:
        model = User
        fields = ('username','first_name','last_name','email', 'password', 'last_login','is_superuser', 'is_staff',
                  'is_active','date_joined')