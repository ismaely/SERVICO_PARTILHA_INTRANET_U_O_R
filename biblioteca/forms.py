from django import forms
from django.forms import ModelForm
from biblioteca.models import Livro



class Livro_Form(ModelForm):
    class Meta:
        model = Livro
        fields = ['titulo', 'autor', 'numero_pagina', 'isbn', 'data_entrada', 'nome']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'autor': forms.TextInput(attrs={'class': 'form-control'}),
            'numero_pagina': forms.TextInput(attrs={'class': 'form-control'}),
            'isbn': forms.TextInput(attrs={'class': 'form-control'}),
            'data_entrada': forms.TextInput(attrs={'type':'date', 'class': 'form-control'}),
            'nome': forms.Select(attrs={'class': 'form-control'}),
        }
