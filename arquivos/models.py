from django.db import models
from helper.opcoes_escolha import PARTILHA_ARQUIVO, TIPOLOGIA




class Arquivo(models.Model):
    titulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=70, blank=True, null=True)
    numero_pagina = models.CharField(max_length=5, null=True, blank=True, default="")
    tipologia = models.CharField(max_length=54, choices=TIPOLOGIA)
    partilha = models.CharField(max_length=20, choices=PARTILHA_ARQUIVO )
    data = models.DateField()
    arquivo = models.FileField(upload_to="arquivos/")

    class Meta:
        ordering = ['titulo']
    def __str__ (self):
        return self.id
