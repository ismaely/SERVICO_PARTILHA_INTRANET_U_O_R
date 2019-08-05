from django.db import models
from helper.opcoes_escolha import (GENERO, PROVINCIA, NIVEL_DOCENTE, NIVEL_FUNCIONARIO, INDIVIAL_GRUPO, MOTIVO_RECLAMACAO, SIMESTRE,
    ANO_ACADEMICO)


# Create your models here.

class Pessoa(models.Model):
    nome = models.CharField(max_length=300)
    data_nascimento = models.CharField(max_length=14)
    bi = models.CharField(max_length=20)
    genero = models.CharField(max_length=20, choices=GENERO)
    provincia = models.CharField(max_length=20, choices=PROVINCIA)
    municipio = models.CharField(max_length=50)
    residencia = models.CharField(max_length=50, null=True, default="--")
    telefone = models.CharField(max_length=20, null=True, default="--")
    email = models.EmailField(null=True, default="--")
    foto = models.FileField(upload_to="foto/", blank=True, null=True, default="user.jpg")
    def __str__ (self):
        return self.id


 

class Aluno(models.Model):
    pessoa= models.ForeignKey(Pessoa, on_delete=models.CASCADE, parent_link=True)
    numero_estudante= models.CharField(max_length=10)
    faculdade = models.CharField(max_length=190)
    curso = models.CharField(max_length=200)
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




class Curso(models.Model):
    nome = models.CharField(max_length=200, unique=True)
    sigla_curso = models.CharField(max_length=20, null=True, default="UOR")
    duracao = models.CharField(max_length=2, null=True, default=" ")

    def __str__ (self):
        return '%s' % (self.nome)



class Disciplina(models.Model):
    nome = models.CharField(max_length=200, default="")
    ano_academico = models.CharField(max_length=200, choices=ANO_ACADEMICO)
    semestre = models.CharField(max_length=200, choices=SIMESTRE)
    carga_horaria = models.CharField(max_length=50, null=True, default="--")

    def __str__ (self):
        return self.nome


class Chaves_Disciplina_Curso(models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, parent_link=True)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE, parent_link=True)
    def __str__ (self):
        return self.id



class Orientador(models.Model):
    docente = models.ForeignKey(Docente, on_delete=models.CASCADE, parent_link=True)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, parent_link=True)
    numero_alunos = models.CharField(max_length=5, default="")
    data_limite = models.CharField(max_length=20, null=True, default="")
    def __str__ (self):
        return self.id



class Nota(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE, parent_link=True)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, parent_link=True)
    disciplina= models.ForeignKey(Disciplina, on_delete=models.CASCADE, parent_link=True)
    data_realizada = models.CharField(max_length=20, null=True, default="")
    data_lancamento = models.CharField(max_length=20, null=True, default="automatico")
    def __str__ (self):
        return self.id




# modelo que reprsenta o tema para defesa
class Tema(models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, parent_link=True)
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE, null=True, blank=True, parent_link=True)
    tema = models.CharField(max_length=100, null=True, default="")
    opcao = models.CharField(max_length=20, choices=INDIVIAL_GRUPO)
    numero_alunos = models.CharField(max_length=3, null=True, blank=True, default="")
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
