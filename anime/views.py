from typing import Any
from django.shortcuts import render, redirect
from  django.views.generic import View, TemplateView, FormView, CreateView
from django.contrib.auth import login, logout, authenticate
from django.db.models import Q
from .models import Usuario, Anime, Comentario
from .forms import UsuarioRegistrarForms, UsuarioEntrarForm
from django.urls import reverse_lazy
from django.shortcuts import render, get_object_or_404

from . models import Anime, User, Comentario
class HomeView(TemplateView):
    template_name = "index.html"
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['listanime'] = Anime.objects.all().order_by("-id")
        
        return context

class RomanceView(TemplateView):
    template_name = "animeromance.html"
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['listanime'] = Anime.objects.filter (Q(genero__icontains = 'romace') | Q(genero__icontains = 'comedia') |Q(genero__icontains = 'ecchi' ))
        
        return context
class AcaoView(TemplateView):
    template_name = "animeacao.html"    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['listanime'] = Anime.objects.filter(Q(genero__icontains = 'Ação') | Q(genero__icontains = 'Isekai')  | Q(genero__icontains = 'Fantasia'))
        return context
class ComentarioView(View):
    
    template_name = 'base.html'

    def get(self, request):
        comentarios = Comentario.objects.all()
        return render(request, self.template_name, {'comentarios': comentarios})

    def post(self, request):
        nome = request.POST.get('nome', '')
        conteudo = request.POST.get('comentar', '')

        if nome and conteudo:
            comentario = Comentario(nome=nome, conteudo=conteudo)

            # Associar o usuário ao comentário se estiver autenticado
            if request.user.is_authenticated:
                comentario.usuario = request.user

            comentario.save()

        comentarios = Comentario.objects.all()
        return render(request, self.template_name, {'comentarios': comentarios})

class ExibirComentarioView(View):
    template_name = 'exibirComentario.html'

    def get(self, request, comentario_id):
        comentario = get_object_or_404(Comentario, pk=comentario_id)
        return render(request, self.template_name, {'comentario': comentario})

class LoginView(FormView):
    template_name = "login.html"
    form_class = UsuarioEntrarForm
    success_url = reverse_lazy("home")
    
    def form_valid(self, form):
        unome = form.cleaned_data.get("username")
        pword = form.cleaned_data.get("password")
        user = authenticate(username= unome, password = pword)
        if user is not None and Usuario.objects.filter(user=user).exists():
            login(self.request, user)
        else:
            return render(self.request, self.template_name, {"form": self.form_class, "error": "Senha e usuario Invalido Tente Novamente!"})

        return super().form_valid(form)
    def get_success_url(self):
        if "next" in self.request.GET:
            next_url = self.request.GET.get("next")
            return next_url
        else:
            return self.success_url

    
    
    
class  sairView(View):
    def get(self , request):
        logout(request)
        return redirect("login")
        
    
    
    

class CadastrarView(CreateView):
    template_name = 'cadastro.html'
    form_class = UsuarioRegistrarForms
    success_url = reverse_lazy("home")
    
    def form_valid(self, form):
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        email = form.cleaned_data.get("email")
        user = User.objects.create_user(username,email,password)
        form.instance.user = user
        login(self.request, user)
        return super().form_valid(form)
    
    def get_success_url(self):
        if "next" in self.request.GET:
            next_url = self.request.GET.get("next")
            return next_url
        else:
            return self.success_url

    

class PesquisaView(TemplateView):
    template_name = "pesquisa.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        kw = self.request.GET.get("keyword")
        results = Anime.objects.filter(Q(titulo__contains=kw) | Q(genero__contains=kw) | Q(genero__contains=kw))
        context["results"] = results
        return context