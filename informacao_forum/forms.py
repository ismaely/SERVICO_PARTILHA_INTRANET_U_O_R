from django import forms
from django.forms import ModelForm
import datetime
from secretaria.models import (Pessoa, Aluno, Docente, Funcionario, Curso, Reclamacao, Orientador, Tema,Matricula, Disciplina_Curso,
Opcao_Matricula, Ano, Nota, Disciplinas)
from helper.opcoes_escolha import (CATEGORIA, NIVEL_DOCENTE, NIVEL_FUNCIONARIO, DIFICIENCIA, PERIODO_MATRICULA2)
from SERVICO_PARTILHA_INTRANET_U_O_R.settings import DATE_INPUT_FORMATS, DATA_ANO, DATA_MES
from helper.core import retorna_id_simples



LISTA_CURSOS = [(k.id, k.nome) for k in Curso.objects.all()]

class Consultar_Form(forms.Form):
    aluno = forms.CharField(max_length=14,  widget=forms.TextInput(attrs={'class': 'form-control'}))
    curso = forms.CharField(max_length=300, widget=forms.Select(choices=LISTA_CURSOS, attrs={'class': 'form-control maiuscula'}))

    def clean_aluno(self):
        aluno = self.cleaned_data.get('aluno')
        bix = retorna_id_simples(aluno)
        if int(bix) > 0:
            return bix
        else:
            raise forms.ValidationError("O Número do aluno não é valido")
