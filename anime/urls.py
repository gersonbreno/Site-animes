from django.urls import path
from . views import *
urlpatterns = [
    path('',  HomeView.as_view() , name="home"),
    path('anime-romace/' , RomanceView.as_view(), name = "romance"), 
    path('cadastrar/' , CadastrarView.as_view(), name = "cadastrar"),
    path('login/' , LoginView.as_view(), name = "login"),
    path('sair/' , sairView.as_view(), name = "sair") , 
    path('animes-acao/' , AcaoView.as_view(), name = "acao") ,
    path('comentario/' ,ComentarioView.as_view(), name = "comentar") ,
    path('exibir-comentario<int:comentario_id>/' ,  ExibirComentarioView.as_view(), name = "exibir") ,
    path('pesquisa/', PesquisaView.as_view(), name='pesquisar'),
]