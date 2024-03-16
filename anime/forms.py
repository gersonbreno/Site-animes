from django import forms
from .models import Usuario, Comentario
from django.forms import ModelForm, TextInput, EmailInput, PasswordInput
from django.contrib.auth.models import User


class UsuarioRegistrarForms(forms.ModelForm):
    username = forms.CharField(widget= forms.TextInput(attrs = {'placeholder': 'usuario', 'class': "form-control", 'style': 'Width: 300px; display: flex; '}))
    password = forms.CharField(widget= forms.PasswordInput (attrs = {'placeholder': 'senha', 'class': "form-control", 'style': 'Width: 300px; display: flex; '}))
    email = forms.CharField(widget= forms.EmailInput(attrs = {'placeholder': 'email@gmail.com', 'class': "form-control", 'style': 'Width: 300px; display: flex; '})) 
    class Meta:
        model = Usuario
        fields = ["username", "password", "email", "nome"]
        widgets= {
           
            'nome': TextInput(attrs={
                'class': "form-control",
                'style': 'width: 300px;',
                'display': 'flex',
                'placeholder': 'nome'

            }),
            
        }
    def clean_password(self):
        password = self.cleaned_data.get("password")
        if len(password) < 8:
            raise forms.ValidationError("A senha deve ter pelo menos 8 caracteres.")
        return password  
    def clean_username(self):
        unome = self.cleaned_data.get("username")
        if User.objects.filter(username = unome).exists():
            raise forms.ValidationError("Este Cliente ja existe no nosso Sistema!")
        return unome
 
class UsuarioEntrarForm(forms.Form):
    username = forms.CharField(widget= forms.TextInput (attrs = {'placeholder': 'usuario', 'class': "form-control", 'style': 'Width: 300px; display: flex; '}))
    password = forms.CharField(widget= forms.PasswordInput (attrs = {'placeholder': 'senha', 'class': "form-control", 'style': 'Width: 300px; display: flex; '}) )

class ComentarioForms(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ["nome", "conteudo"]
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'conteudo': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }