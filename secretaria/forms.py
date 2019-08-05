from django import forms
from django.forms import ModelForm
import datetime
from secretaria.models import (Pessoa, Aluno, Docente, Funcionario, Curso, Disciplina, Reclamacao, Orientador, Tema)
from helper.opcoes_escolha import (GENERO, PROVINCIA, CATEGORIA, NIVEL_DOCENTE, NIVEL_FUNCIONARIO)
from SERVICO_PARTILHA_INTRANET_U_O_R.settings import DATE_INPUT_FORMATS


class PessoaForm(ModelForm):
    nome = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control '}))
    data_nascimento = forms.CharField(widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control '}))
    bi = forms.CharField(max_length=14, widget=forms.TextInput(attrs={'class': 'form-control bi_mask'}))
    genero = forms.CharField(max_length=12, widget=forms.Select(choices=GENERO,attrs={'class': 'form-control '}))
    provincia = forms.CharField(max_length=25, widget=forms.Select(choices=PROVINCIA, attrs={'class': 'form-control'}))
    municipio = forms.CharField(max_length=30, required=False, widget=forms.Select(choices='', attrs={'class': 'form-control'}))
    residencia = forms.CharField(max_length=60, required=False, widget=forms.TextInput(attrs={'class': 'form-control '}))
    telefone = forms.CharField(max_length=12, required=False, widget=forms.TextInput(attrs={'class': 'form-control' }))
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



class CursoForm(ModelForm):
    nome = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    sigla_curso = forms.CharField(max_length=50, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    duracao = forms.CharField(max_length=2, widget=forms.TextInput(attrs={'class': 'form-control'}))
    class Meta:
        model = Curso
        fields = ['nome', 'sigla_curso', 'duracao']



class DisciplinaForm(ModelForm):
    class Meta:
        model = Disciplina
        fields = ['nome', 'ano_academico', 'semestre', 'carga_horaria']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'ano_academico': forms.Select(attrs={'class': 'form-control'}),
            'semestre': forms.Select(attrs={'class': 'form-control'}),
            'carga_horaria': forms.TextInput(attrs={'class': 'form-control'}),
        }



class ReclamacaoForm(ModelForm):
    class Meta:
        model = Reclamacao
        fields = ('aluno', 'curso', 'motivo', 'descricao')
        widgets = {
            'aluno': forms.TextInput( attrs={'required': "" ,'class': 'form-control'}),
            'curso': forms.Select(attrs={'class': 'form-control'}),
            'motivo': forms.Select(attrs={'class': 'form-control'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control', 'length': 4500})
        }



class Orientador_TeseForm(ModelForm):
    class Meta:
        model = Orientador
        fields = ('docente', 'curso', 'numero_alunos', 'data_limite')
        widgets = {
            'numero_alunos': forms.TextInput( attrs={'required': "" ,'class': 'form-control'}),
            'curso': forms.Select(attrs={'class': 'form-control'}),
            'docente': forms.Select(attrs={'class': 'form-control'}),
            'data_limite': forms.TextInput(attrs={'type':'date', 'class': 'form-control'})
        }



class TemasForm(ModelForm):
    aluno = forms.CharField(max_length=14, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    numero_alunos = forms.CharField(max_length=3, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    descricao = forms.CharField(max_length=1500, required=False, widget=forms.Textarea(attrs={'class': 'form-control', 'id':'message'}))
    class Meta:
        model = Tema
        fields = ('curso', 'numero_alunos', 'tema', 'opcao', 'data_entrada', 'situacao', 'descricao')
        widgets = {
            'curso': forms.Select(attrs={'class': 'form-control'}),
            'tema': forms.TextInput(attrs={'class': 'form-control'}),
            'opcao': forms.Select(attrs={'class': 'form-control'}),
            'data_entrada': forms.TextInput(attrs={'type':'date', 'class': 'form-control'}),
        }
