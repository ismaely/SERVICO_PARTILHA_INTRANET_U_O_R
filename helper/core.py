from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.graphics.shapes import Drawing, Line
from reportlab.lib.units import inch, mm
from SERVICO_PARTILHA_INTRANET_U_O_R.settings import DATA_HORA_ZONA
from django.conf import settings
import base64, random, sweetify, os
from secretaria.models import (Pessoa, Aluno, Docente, Funcionario, Curso, Orientador, Tema, Reclamacao)

SOFIL_WEB = '<a href>SOFIL-WEB</a>'

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
        value =request.POST['aluno']
        print(value)
        lu = Aluno.objects.get(pessoa__bi=value)
        if lu.id:
            return lu.id
    except Aluno.DoesNotExist:
        try:
            resp = Aluno.objects.get(numero_estudante=value)
            if resp.id:
                return resp.id
        except Aluno.DoesNotExist:
            sweetify.error(request,'O Numero de Aluno não é valido!!....', timer='4900', button='Ok', footer=SOFIL_WEB)
            return 0


# função q retorna o id em função bi ou numero de estudante
def retorna_id_simples(value):
    try:
        lu = Aluno.objects.get(pessoa__bi=value)
        if lu.id is not None:
            return lu.id
    except Aluno.DoesNotExist:
        try:
            resp = Aluno.objects.get(numero_estudante=value)
            if resp.id:
                return resp.id
        except Aluno.DoesNotExist:
            return 0



# RODAPE QUE PRECHE A FICHA DE MATRICULA EM PDF
def rodape_ficha_matricula(canvas, doc):
    logo = os.path.join(settings.MEDIA_ROOT, str('logo/Logotipo Principal.jpg'))
    canvas.drawImage(logo, 12, 535, width=290, height=255, mask=None)
    canvas.drawString(269,39*mm,'Operador')
    canvas.line(188,32*mm,406,32*mm)
    page_num = canvas.getPageNumber()
    #text = "Pagina #%s" % page_num
    #canvas.drawRightString(200*mm, 20*mm, text)
