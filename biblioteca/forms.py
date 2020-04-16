from django import forms
from django.forms import ModelForm
from biblioteca.models import Livro, Solicitacao
from helper.core import retorna_id_simples



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


class Solicitacao_Obra_Form(ModelForm):
    aluno = forms.CharField(max_length=14, widget=forms.TextInput(attrs={'class': 'form-control'}))
    class Meta:
        model = Solicitacao
        fields = ['titulo', 'autor', 'data_entrada', 'categoria', 'quantidade']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'autor': forms.TextInput(attrs={'class': 'form-control'}),
            'data_entrada': forms.TextInput(attrs={'type':'date', 'class': 'form-control'}),
            'categoria': forms.Select(attrs={'class': 'form-control'}),
            'quantidade': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def clean_aluno(self):
        aluno = self.cleaned_data.get('aluno')
        id = retorna_id_simples(aluno)
        if id is not None and int(id) > 0:
            return id
        raise forms.ValidationError(" O número do BI não é valido, não existe")
