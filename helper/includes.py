#ficheiro onde vai constar todos include que seram usado
from django.shortcuts import render
from django.http import HttpResponseRedirect, JsonResponse, HttpRequest, Http404, HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

from django.urls import reverse
from django.views import generic
import sweetify
import base64

from SERVICO_PARTILHA_INTRANET_U_O_R.settings import DATA_HORA_ZONA
import helper.core
from helper.opcoes_escolha import (GENERO, PROVINCIA, NIVEL_DOCENTE, NIVEL_FUNCIONARIO, BENGO, BENGUELA, BIE, CABINDA, CUANDO_CUBANGO, CUNENE, HUAMBO, HUILA, CUANZA_NORTE, CUANZA_SUL, LUANDA,
    LUNDA_NORTE, LUNDA_SUL, MALANJE, MOXICO, NAMIBE, UIGE, ZAIRE, INDIVIAL_GRUPO, MOTIVO_RECLAMACAO)


# importção da Secretaria
from secretaria.models import Pessoa, Aluno, Docente, Funcionario
from secretaria.forms import AlunoForm, DocenteForm, PessoaForm, DocenteForm, FuncionarioForm
