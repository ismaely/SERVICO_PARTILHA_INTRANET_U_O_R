from django.db import models
from helper.opcoes_escolha import GENERO, PROVINCIA


# Create your models here.

class Pessoa(models.Model):
    nome = models.CharField(max_length=300)
    data_nascimento = models.CharField(max_length=14)
    bi = models.CharField(max_length=20)
    genero = models.CharField(max_length=20, choices=GENERO)
    provincia = models.CharField(max_length=20, choices=PROVINCIA)
    municipio = models.CharField(max_length=50)
    residencia = models.CharField(max_length=50)
    telefone = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__ (self):
        return self.id
