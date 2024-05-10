from django.urls import path
from . views import *
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
urlpatterns = [
    path('',  HomeView.as_view() , name="home"),
    path('anime-romace/' , RomanceView.as_view(), name = "romance"), 
    path('cadastrar/' , CadastrarView.as_view(), name = "cadastrar"),
    path('login/' , LoginView.as_view(), name = "login"),
    path('sair/' , sairView.as_view(), name = "sair") , 
    path('animes-acao/' , AcaoView.as_view(), name = "acao") ,
    path('pesquisa/', PesquisaView.as_view(), name='pesquisar'),
    # path('comentar/<int:post_id>/', ComentarioView.as_view(), name='comentar'),
    path('comentar/', ComentarioView.as_view(), name='comentar'),
    path('reset_password/', PasswordResetView.as_view(), name='password_reset'),
    path('reset_password_sent/', PasswordResetDoneView.as_view(template_name='password/sent.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name='password/form.html'), name='password_reset_confirm'),
    path('reset_password_complete/', PasswordResetCompleteView.as_view(template_name='password/done.html'), name='password_reset_complete'),
]