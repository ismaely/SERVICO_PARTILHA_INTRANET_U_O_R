from django.db import models
from helper.opcoes_escolha import (GENERO, PROVINCIA, NIVEL_DOCENTE, NIVEL_FUNCIONARIO, INDIVIAL_GRUPO, MOTIVO_RECLAMACAO,
    PERIODO_MATRICULA, ESTADO_CIVIL, DIFICIENCIA)


# Create your models here.


# modelos se  ajuda , nivel academico
class Ano(models.Model):
    nome = models.CharField(max_length=20)

    def __str__ (self):
        return "%s" % (self.nome)


# modelo semestre para definir os semestres
class Semestre(models.Model):
    nome = models.CharField(max_length=30)
    def __str__ (self):
        return "%s" % (self.nome)


# modelos se  ajuda , OPÇÃO DE MARICULA
class Opcao_Matricula(models.Model):
    nome = models.CharField(max_length=50)

    def __str__ (self):
        return "%s" % (self.nome)

# modelos se  ajuda , PARA DESCRIÇÃO DA NOTA
class Descricao_Nota(models.Model):
    valor = models.CharField(max_length=2, unique=True)
    nome = models.CharField(max_length=50)

    def __str__ (self):
        return "%s" % (self.nome)


class Curso(models.Model):
    nome = models.CharField(max_length=200, unique=True)
    sigla_curso = models.CharField(max_length=20, null=True, default="UOR")
    duracao = models.CharField(max_length=2, null=True, default=" ")

    def __str__ (self):
        return '%s' % (self.nome)



class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    nome_pai = models.CharField(max_length=100, blank=True, null=True, default="--")
    nome_mae = models.CharField(max_length=100, blank=True, null=True, default="--")
    data_nascimento = models.CharField(max_length=14)
    bi = models.CharField(max_length=20)
    passaporte = models.CharField(max_length=30, blank=True, null=True, default=" ")
    genero = models.CharField(max_length=20, choices=GENERO)
    provincia = models.CharField(max_length=20, choices=PROVINCIA)
    municipio = models.CharField(max_length=50)
    residencia = models.CharField(max_length=50, null=True, default="--")
    bairro = models.CharField(max_length=80, null=True, default="--")
    telefone = models.CharField(max_length=20, null=True, default="--")
    email = models.EmailField(null=True, default="--")
    estado_civil = models.CharField(max_length=20, choices=ESTADO_CIVIL)
    dificiencia = models.CharField(max_length=20,blank=True, null=True, choices=DIFICIENCIA)
    especifica_dificiencia = models.CharField(max_length=250, blank=True, null=True, default="")
    foto = models.FileField(upload_to="foto/", blank=True, null=True, default="user.jpg")

    def __str__ (self):
        return self.id




class Aluno(models.Model):
    pessoa= models.ForeignKey(Pessoa, on_delete=models.CASCADE, parent_link=True)
    numero_estudante= models.CharField(max_length=10)
    categoria = models.CharField(max_length=20, null=True, default="ESTUDANTE")

    def __str__ (self):
        return '%d' % (self.id)



class Docente(models.Model):
    pessoa= models.ForeignKey(Pessoa, on_delete=models.CASCADE, parent_link=True)
    numero_docente= models.CharField(max_length=10, null=True)
    categoria = models.CharField(max_length=20, null=True, default="DOCENTE")
    nivel_academico = models.CharField(max_length=50, choices=NIVEL_DOCENTE)

    def __str__ (self):
        return '%s'  % (self.pessoa.nome)


class Funcionario(models.Model):
    pessoa= models.ForeignKey(Pessoa, on_delete=models.CASCADE, parent_link=True)
    cargo = models.CharField(max_length=50, null=True)
    categoria = models.CharField(max_length=20, null=True, default="FUNCIONARIO")
    nivelacademico = models.CharField(max_length=50, choices=NIVEL_FUNCIONARIO)
    def __str__ (self):
        return self.id


class Disciplinas(models.Model):
    nome = models.CharField(max_length=200, default="")
    carga_horaria = models.CharField(max_length=50, null=True, default="--")

    def __str__ (self):
        return '%s'  % (self.nome)
        #return self.nome


class Orientador(models.Model):
    docente = models.ForeignKey(Docente, on_delete=models.CASCADE, parent_link=True)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, parent_link=True)
    data_limite = models.CharField(max_length=20, null=True, default="")
    def __str__ (self):
        return self.id



# modelo que reprsenta o tema para defesa
class Tema(models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, parent_link=True)
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE, null=True, blank=True, parent_link=True)
    tema = models.CharField(max_length=100, null=True, default="")
    opcao = models.CharField(max_length=20, choices=INDIVIAL_GRUPO)
    #numero_alunos = models.CharField(max_length=3, null=True, blank=True, default="")
    situacao = models.CharField(max_length=30, null=True, blank=True, default="Aprovado")
    data_entrada = models.DateField()
    descricao = models.TextField(max_length=1900, null=True, blank=True, default="")

    class Meta:
        ordering = ['situacao']
    def __str__ (self):
        return self.id


class Monografia(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE, parent_link=True)
    tema = models.ForeignKey(Tema, on_delete=models.CASCADE, parent_link=True)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, parent_link=True)
    opcao = models.CharField(max_length=20, choices=INDIVIAL_GRUPO)
    opcao_aprovacao = models.CharField(max_length=20, null=True, default="Em Analise")
    data_entrada = models.DateField()
    def __str__ (self):
        return self.id


class Defesa_Monografia(models.Model):
    docente = models.ForeignKey(Docente, on_delete=models.CASCADE, parent_link=True)
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE, parent_link=True)
    monografia= models.ForeignKey(Monografia, on_delete=models.CASCADE, parent_link=True)
    nota_final = models.CharField(max_length=2, null=True, default="0")
    opcao_final = models.CharField(max_length=20, null=True, default="Final")
    data_defesa = models.DateField()
    def __str__ (self):
        return self.id


# modelo Reclamação
class Reclamacao(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE, parent_link=True)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, parent_link=True)
    motivo = models.CharField(max_length=20, choices=MOTIVO_RECLAMACAO)
    data = models.DateField(auto_now_add=True, blank=False, null=True)
    estado = models.CharField(max_length=20, null=True, default="Em Analise")
    descricao = models.CharField(max_length=3000, null=True, default="")

    def __str__ (self):
        return self.id




class Nota(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE, parent_link=True)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, parent_link=True)
    ano = models.ForeignKey(Ano, on_delete=models.CASCADE, parent_link=True)
    semestre = models.ForeignKey(Semestre, on_delete=models.CASCADE, parent_link=True)
    descricao = models.ForeignKey(Descricao_Nota, on_delete=models.CASCADE,  parent_link=True)
    disciplina= models.ForeignKey(Disciplinas, on_delete=models.CASCADE, parent_link=True)
    data_realizada = models.CharField(max_length=20, null=True, default="")
    data_automatico = models.DateField(auto_now=True)
    nota = models.CharField(max_length=2)


    def __str__ (self):
        return self.id



class Matricula(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE, parent_link=True)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, parent_link=True)
    opcao_matricula = models.ForeignKey(Opcao_Matricula, on_delete=models.CASCADE, parent_link=True)
    ano = models.ForeignKey(Ano, on_delete=models.CASCADE, parent_link=True)
    semestre = models.ForeignKey(Semestre, on_delete=models.CASCADE, parent_link=True)
    data = models.DateField(max_length=20)
    nota_exame = models.CharField(max_length=2, null=True,blank=True, default=" ")
    periodo = models.CharField(max_length=20, choices=PERIODO_MATRICULA)

    def __str__ (self):
        return self.id


# modelo onde vai se juntar o id da disciplina e do curso , pois é a relação de muitos para muito
class Disciplina_Curso(models.Model):
    ano = models.ForeignKey(Ano, on_delete=models.CASCADE, parent_link=True)
    semestre = models.ForeignKey(Semestre, on_delete=models.CASCADE, parent_link=True)
    disciplina = models.ForeignKey(Disciplinas, on_delete=models.CASCADE, parent_link=True)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, parent_link=True)

    def __str__ (self):
        return self.id
