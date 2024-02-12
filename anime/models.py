from django.db import models
from django.contrib.auth.models import User

class Usuario(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    nome = models.CharField(max_length = 100)
    email = models.EmailField()

    def __str__(self):
        return self.nome


class Anime(models.Model):
    
    titulo = models.CharField(max_length = 150, null = False)
    img = models.ImageField(upload_to="anime")
    genero = models.CharField(max_length = 200)
    snipose = models.TextField()
    
    

    def __str__(self) :
        return "Categrias" +  str(self.id)

    
class Comentario(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete = models.CASCADE)
    nome = models.CharField(max_length = 50, default='Nome ')
    conteudo = models.TextField()
    data_publicao = models.DateField(auto_now_add = True)
    def __str__(self):
        return "Usuario" +  str(self.id)