from django import forms
from django.forms import ModelForm
from secretaria.models import Pessoa, Aluno, Docente, Funcionario
from helper.opcoes_escolha import GENERO, PROVINCIA, CATEGORIA, NIVEL_DOCENTE, NIVEL_FUNCIONARIO


class PessoaForm(ModelForm):
    nome = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control '}))
    data_nascimento = forms.CharField(widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control '}))
    bi = forms.CharField(max_length=14, widget=forms.TextInput(attrs={'class': 'form-control bi_mask'}))
    genero = forms.CharField(max_length=12, widget=forms.Select(choices=GENERO,attrs={'class': 'form-control '}))
    provincia = forms.CharField(max_length=25, widget=forms.Select(choices=PROVINCIA, attrs={'class': 'form-control'}))
    municipio = forms.CharField(max_length=30, required=False, widget=forms.Select(choices='', attrs={'class': 'form-control'}))
    residencia = forms.CharField(max_length=60, widget=forms.TextInput(attrs={'class': 'form-control '}))
    telefone = forms.CharField(max_length=18, required=False, widget=forms.TextInput(attrs={'class': 'form-control' }))
    email = forms.EmailField(max_length=80, required=False, widget=forms.TextInput(attrs={'class': 'form-control '}))
    foto = forms.CharField(required=False, widget=forms.TextInput(attrs={'type':'hidden', 'class': 'form-control', 'id': 'salva1'}))
    categoria = forms.CharField(max_length=25, widget=forms.Select(choices=CATEGORIA, attrs={'class': 'form-control '}))
    class Meta:
        model = Pessoa
        fields = ['nome',  'data_nascimento', 'bi', 'genero','provincia', 'municipio', 'residencia', 'telefone', 'email', 'foto']



class AlunoForm(ModelForm):
    numero_estudante = forms.CharField(max_length=10, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    faculdade = forms.CharField(max_length=14,required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    curso = forms.CharField(max_length=200, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    categoria = forms.CharField(max_length=25, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    class Meta:
        model = Aluno
        fields = ['numero_estudante', 'faculdade', 'curso', 'categoria']




class DocenteForm(ModelForm):
    numero_docente = forms.CharField(max_length=10, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    categoria = forms.CharField(max_length=25, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    nivel_academico = forms.CharField(max_length=90, widget=forms.Select(choices=NIVEL_DOCENTE, attrs={'class': 'form-control'}))
    class Meta:
        model = Docente
        fields = ['numero_docente', 'categoria', 'nivel_academico']



class FuncionarioForm(ModelForm):
    cargo = forms.CharField(max_length=10, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    categoria = forms.CharField(max_length=25, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    nivelacademico = forms.CharField(max_length=90, widget=forms.Select(choices=NIVEL_FUNCIONARIO, attrs={'class': 'form-control'}))
    class Meta:
        model = Funcionario
        fields = ['cargo', 'categoria', 'nivelacademico']
