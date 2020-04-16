from django import forms
from django.forms import ModelForm
import datetime
from secretaria.models import (Pessoa, Aluno, Docente, Funcionario, Curso, Reclamacao, Orientador, Tema, Matricula, Disciplina_Curso,
Opcao_Matricula, Ano, Nota, Disciplinas)
from helper.opcoes_escolha import (GENERO, PROVINCIA, CATEGORIA, NIVEL_DOCENTE, NIVEL_FUNCIONARIO, ESTADO_CIVIL, DIFICIENCIA, PERIODO_MATRICULA2)
from SERVICO_PARTILHA_INTRANET_U_O_R.settings import DATE_INPUT_FORMATS, DATA_ANO, DATA_MES
from helper.core import retorna_id_simples



OPCAO_MATRICULA = []
ANO = []
ANO.append(['','-------'])
OPCAO_MATRICULA.append(['','-------'])
for item in Opcao_Matricula.objects.all():
    OPCAO_MATRICULA.append([int(item.id), str(item.nome)])
for item in Ano.objects.all():
    ANO.append([int(item.id), str(item.nome)])



class PessoaForm(ModelForm):
    nome = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control maiuscula'}))
    nome_pai = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={'class': 'form-control maiuscula'}))
    nome_mae = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={'class': 'form-control maiuscula'}))
    data_nascimento = forms.CharField(widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control '}))
    bi = forms.CharField(max_length=14, widget=forms.TextInput(attrs={'class': 'form-control bi_mask maiuscula'}))
    passaporte = forms.CharField(max_length=30, required=False, widget=forms.TextInput(attrs={'class': 'form-control maiuscula'}))
    genero = forms.CharField(max_length=12, widget=forms.Select(choices=GENERO,attrs={'class': 'form-control maiuscula'}))
    provincia = forms.CharField(max_length=25, widget=forms.Select(choices=PROVINCIA, attrs={'class': 'form-control'}))
    municipio = forms.CharField(max_length=30, required=False, widget=forms.Select(choices='', attrs={'class': 'form-control'}))
    residencia = forms.CharField(max_length=60, required=False, widget=forms.TextInput(attrs={'class': 'form-control maiuscula'}))
    telefone = forms.CharField(max_length=12, required=False, widget=forms.TextInput(attrs={'class': 'form-control' }))
    email = forms.EmailField(max_length=80, required=False, widget=forms.TextInput(attrs={'class': 'form-control '}))
    foto = forms.CharField(required=False, widget=forms.TextInput(attrs={'type':'hidden', 'class': 'form-control', 'id': 'salva1'}))
    categoria = forms.CharField(max_length=25, required=False, widget=forms.Select(choices=CATEGORIA, attrs={'class': 'form-control '}))
    class Meta:
        model = Pessoa
        fields = ['nome',  'data_nascimento', 'bi', 'genero','provincia', 'municipio', 'residencia', 'telefone', 'email', 'foto', 'estado_civil', 'bairro', 'dificiencia', 'nome_pai', 'nome_mae', 'passaporte', 'especifica_dificiencia']
        widgets = {
            'bairro': forms.TextInput(attrs={'class': 'form-control maiuscula'}),
            'estado_civil': forms.Select(attrs={'class': 'form-control'}),
            'dificiencia': forms.Select(attrs={'class': 'form-control', 'id': 'dificiencia_ajax'}),
            'especifica_dificiencia': forms.TextInput(attrs={'class': 'form-control especifica_ajax'}),
        }
    def clean_data_nascimento(self):
        data_nascimento = self.cleaned_data.get('data_nascimento')
        data = []
        data = data_nascimento.split('-')
        total = int(DATA_ANO) - int(data[0])

        if int(total) < 17:
            raise forms.ValidationError("não é valido a data de nascimento, é menor de idade")
        else:
            return data_nascimento



class AlunoForm(ModelForm):
    numero_estudante = forms.CharField(max_length=10, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    faculdade = forms.CharField(max_length=14,required=False, widget=forms.TextInput(attrs={'class': 'form-control maiuscula'}))
    curso = forms.CharField(max_length=200, required=False, widget=forms.TextInput(attrs={'class': 'form-control maiuscula'}))
    categoria = forms.CharField(max_length=25, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    class Meta:
        model = Aluno
        fields = ['numero_estudante', 'faculdade', 'curso', 'categoria']




class DocenteForm(ModelForm):
    numero_docente = forms.CharField(max_length=10, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    categoria = forms.CharField(max_length=25, required=False, widget=forms.TextInput(attrs={'class': 'form- maiuscula'}))
    nivel_academico = forms.CharField(max_length=90, widget=forms.Select(choices=NIVEL_DOCENTE, attrs={'class': 'form-control maiuscula'}))
    class Meta:
        model = Docente
        fields = ['numero_docente', 'categoria', 'nivel_academico']



class FuncionarioForm(ModelForm):
    cargo = forms.CharField(max_length=10, required=False, widget=forms.TextInput(attrs={'class': 'form-control maiuscula'}))
    categoria = forms.CharField(max_length=25, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    nivelacademico = forms.CharField(max_length=90, widget=forms.Select(choices=NIVEL_FUNCIONARIO, attrs={'class': 'form-control'}))
    class Meta:
        model = Funcionario
        fields = ['cargo', 'categoria', 'nivelacademico']



class CursoForm(ModelForm):
    nome = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    sigla_curso = forms.CharField(max_length=50, required=False, widget=forms.TextInput(attrs={'class': 'form-control maiuscula'}))
    duracao = forms.CharField(max_length=2, required=False,widget=forms.TextInput(attrs={'class': 'form-control'}))
    class Meta:
        model = Curso
        fields = ['nome', 'sigla_curso', 'duracao']



class DisciplinaForm(ModelForm):
    class Meta:
        model = Disciplinas
        fields = ['nome', 'carga_horaria']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control maiuscula'}),
            'carga_horaria': forms.TextInput(attrs={'class': 'form-control'}),
        }



class ReclamacaoForm(ModelForm):
    class Meta:
        model = Reclamacao
        fields = ('aluno', 'curso', 'motivo', 'descricao')
        widgets = {
            'aluno': forms.TextInput( attrs={'required': "" ,'class': 'form-control'}),
            'curso': forms.Select(attrs={'class': 'form-control maiuscula'}),
            'motivo': forms.Select(attrs={'class': 'form-control'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control', 'length': 4500})
        }



class Orientador_TeseForm(ModelForm):
    class Meta:
        model = Orientador
        fields = ('docente', 'curso', 'data_limite')
        widgets = {
            'curso': forms.Select(attrs={'class': 'form-control maiuscula'}),
            'docente': forms.Select(attrs={'class': 'form-control'}),
            'data_limite': forms.TextInput(attrs={'type':'date', 'class': 'form-control'})
        }



class TemasForm(ModelForm):
    aluno = forms.CharField(max_length=14, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    #numero_alunos = forms.CharField(max_length=3, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    descricao = forms.CharField(max_length=1500, required=False, widget=forms.Textarea(attrs={'class': 'form-control', 'id':'message'}))
    class Meta:
        model = Tema
        fields = ('curso', 'tema', 'opcao', 'data_entrada', 'situacao', 'descricao')
        widgets = {
            'curso': forms.Select(attrs={'class': 'form-control'}),
            'tema': forms.TextInput(attrs={'class': 'form-control'}),
            'opcao': forms.Select(attrs={'class': 'form-control'}),
            'data_entrada': forms.TextInput(attrs={'type':'date', 'class': 'form-control'}),
        }



class MatriculaForm(ModelForm):
    aluno = forms.CharField(max_length=14, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    #numero_alunos = forms.CharField(max_length=3, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    class Meta:
        model = Matricula
        fields = ('curso', 'ano', 'data', 'nota_exame', 'periodo', 'opcao_matricula', 'semestre')
        widgets = {
            'curso': forms.Select(attrs={'class': 'form-control'}),
            'nota_exame': forms.TextInput(attrs={'class': 'form-control'}),
            'opcao_matricula': forms.Select(attrs={'class': 'form-control'}),
            'ano': forms.Select(attrs={'class': 'form-control'}),
            'semestre': forms.Select(attrs={'class': 'form-control'}),
            'periodo': forms.Select(attrs={'class': 'form-control'}),
            'data': forms.TextInput(attrs={'type':'date', 'class': 'form-control'}),
        }

    def clean_aluno(self):
        aluno = self.cleaned_data.get('aluno')
        bix = retorna_id_simples(aluno)
        if int(bix) > 0:
            return bix
        else:
            raise forms.ValidationError("O Número do aluno não é valido")

    def clean_nota_exame(self):
        opcao_matricula = self.cleaned_data.get('opcao_matricula')
        nota_exame = self.cleaned_data.get('nota_exame')
        if opcao_matricula == '1':
            raise forms.ValidationError(" A Nota do exame é obrigatorio!")
        return nota_exame


class Lancamento_nota_Form(ModelForm):
    aluno = forms.CharField(max_length=14, widget=forms.TextInput(attrs={'class': 'form-control col-md-7 col-xs-12'}))
    disciplina = forms.CharField(widget=forms.Select(choices='', attrs={'class': 'form-control ajax_disciplina col-md-7 col-xs-12'}))
    class Meta:
        model = Nota
        fields = ('curso', 'data_realizada', 'nota', 'ano', 'semestre')
        widgets = {
            'curso': forms.Select(attrs={'class': 'form-control col-md-7 col-xs-12 ajax_curso_nota'}),
            'nota': forms.TextInput(attrs={'class': 'form-control col-md-7 col-xs-12'}),
            'data_realizada': forms.TextInput(attrs={'type':'date', 'class': 'form-control'}),
            'ano': forms.Select(attrs={'class': 'form-control ajax_ano_nota'}),
            'semestre': forms.Select(attrs={'class': 'form-control ajax_semestre_nota'}),
        }

    def clean_aluno(self):
        aluno = self.cleaned_data.get('aluno')
        bix = retorna_id_simples(aluno)
        if int(bix) > 0:
            return bix
        else:
            raise forms.ValidationError("O Número do aluno não é valido")

    def clean_nota(self):
        nota = self.cleaned_data.get('nota')
        if int(nota) < 0  or int(nota) > 20:
            raise forms.ValidationError("A Nota não é valida")
        return nota



# Formulario que vai adicioar a disciplina no curso, associação de muitos para muitos
class Disciplina_Curso_Form(ModelForm):
    class Meta:
        model = Disciplina_Curso
        fields = ('curso', 'disciplina', 'ano', 'semestre')
        widgets = {
            'disciplina': forms.Select(attrs={'class': 'form-control'}),
            'curso': forms.Select(attrs={'class': 'form-control'}),
            'ano': forms.Select(attrs={'class': 'form-control'}),
            'semestre': forms.Select(attrs={'class': 'form-control'}),
        }


# formulario que vai listar os cursos, que vai permitir listar as disciplinas de cada curso
class Listar_Disciplinas_CadaCurso_Form(ModelForm):
    class Meta:
        model = Disciplina_Curso
        fields = ('curso',)
        widgets = {
            'curso': forms.Select(attrs={'class': 'form-control'}),
        }



class Listar_Estudante_MatriculaForm(ModelForm):
    data_final= forms.CharField(required=False, widget=forms.DateInput(attrs={'type': 'date'}))
    data= forms.CharField(required=False, widget=forms.DateInput(attrs={'type': 'date'}))
    opcao_matricula = forms.CharField(required=False, max_length=25, widget=forms.Select(choices=OPCAO_MATRICULA, attrs={'class': 'form-control'}))
    periodo = forms.CharField(required=False, max_length=25, widget=forms.Select(choices=PERIODO_MATRICULA2, attrs={'class': 'form-control'}))
    ano_frequencia = forms.CharField(required=False, max_length=25, widget=forms.Select(choices=ANO, attrs={'class': 'form-control'}))
    class Meta:
        model = Matricula
        fields = ('curso', 'ano_frequencia', 'periodo', 'opcao_matricula')
        widgets = {
            'curso': forms.Select(attrs={'class': 'form-control'}),
        }
