from SERVICO_PARTILHA_INTRANET_U_O_R.settings import DATA_HORA_ZONA
import random
import base64
import sweetify
from secretaria.models import (Pessoa, Aluno, Docente, Funcionario, Curso, Disciplina, Orientador, Tema, Reclamacao)



# função que vai prepara a foto
def prepara_foto(request):
    nome = str(DATA_HORA_ZONA).split('.')
    img = request.POST["foto"]
    foto = []
    inicio = img.find(',')
    imagem = img[inicio+1:]
    with open("./media/foto/" + str(nome[0]) + "_" + str(random.random()) + ".png", "wb") as fh:
        fh.write(base64.b64decode(imagem))
        foto = str(fh).split('=')
        um = foto[1].replace(">", '')
    um = um.replace("'", '')
    um = um.split('media/')
    return um[1]



#função que vai retorna o id do aluno ou pessoa em função do bi o numero de estudante
def retorna_id(request):
   try:
      value =request.POST['numero_alunos']
      bi = Pessoa.objects.get(bi=value)
      if bi.id is not None:
         lu = Aluno.objects.get(id=bi.id)
         return lu.id
   except Pessoa.DoesNotExist:
       try:
          alu = Aluno.objects.get(numero_estudante=value)
          return alu.id
       except Aluno.DoesNotExist:
          sweetify.success(request,'O Numero de Estudante não é valido!....', timer='4900', button='Ok', footer=SOFIL_WEB)
          return 0
