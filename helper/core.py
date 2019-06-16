from SERVICO_PARTILHA_INTRANET_U_O_R.settings import DATA_HORA_ZONA
import random
import base64


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
