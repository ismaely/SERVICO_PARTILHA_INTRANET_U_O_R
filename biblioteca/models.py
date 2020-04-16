from django.db import models
from secretaria.models import  Aluno

# Create your models here.


class Categoria_livro(models.Model):
    nome = models.CharField(max_length=100,null=True, blank=True, default="")
    class Meta:
        ordering = ['nome']
    def __str__ (self):
        return "%s" % (self.nome)



class Livro(models.Model):
    nome = models.ForeignKey(Categoria_livro, on_delete=models.SET_NULL, blank=True, null=True, parent_link=True)
    titulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)
    numero_pagina = models.CharField(max_length=5, null=True, blank=True, default="")
    isbn = models.CharField(max_length=14, null=True, blank=True, default="")
    data_entrada = models.DateField()

    class Meta:
        ordering = ['titulo']
    def __str__ (self):
        return self.id



class Solicitacao(models.Model):
    categoria = models.ForeignKey(Categoria_livro, on_delete=models.SET_NULL, blank=True, null=True, parent_link=True)
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE, parent_link=True)
    titulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)
    quantidade = models.CharField(max_length=2)
    data_entrada = models.DateField()
    estado = models.CharField(max_length=30, blank=True, null=True, default="Recebido")

    class Meta:
        ordering = ['titulo']
    def __str__ (self):
        return self.id
