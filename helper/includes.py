#ficheiro onde vai constar todos include que seram usado
from django.shortcuts import render
from django.http import HttpResponseRedirect, JsonResponse, HttpRequest, Http404, HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout
from django.db.models import Q
from datetime import datetime, date

from django.urls import reverse
from django.views import generic
import sweetify, json, base64
from sweetify.views import SweetifySuccessMixin

#biblioteca para cria PDF
import random, json, re, os, sweetify, reportlab, qrcode
from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.graphics.shapes import Drawing, Line
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch, mm
from reportlab.lib.utils import ImageReader
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4, B4, cm, letter, landscape
from reportlab.platypus import (Image, PageBegin, PageBreak, Paragraph, Table,tables, TableStyle, SimpleDocTemplate,
 Spacer, NextPageTemplate, Frame, PageTemplate)
from reportlab.rl_config import defaultPageSize
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT, TA_RIGHT
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics, ttfonts

from SERVICO_PARTILHA_INTRANET_U_O_R.settings import DATA_HORA_ZONA
import helper.core
from helper.opcoes_escolha import (GENERO, PROVINCIA, NIVEL_DOCENTE, NIVEL_FUNCIONARIO, BENGO, BENGUELA, BIE, CABINDA, CUANDO_CUBANGO, CUNENE, HUAMBO, HUILA, CUANZA_NORTE, CUANZA_SUL, LUANDA,
    LUNDA_NORTE, LUNDA_SUL, MALANJE, MOXICO, NAMIBE, UIGE, ZAIRE, INDIVIAL_GRUPO, MOTIVO_RECLAMACAO, MESES)


# importção da Secretaria
from secretaria.models import (Pessoa, Aluno, Docente, Funcionario, Curso, Orientador, Tema, Reclamacao, Matricula, Disciplina_Curso, Disciplinas, Descricao_Nota, Nota)

from secretaria.forms import (AlunoForm, DocenteForm, PessoaForm, DocenteForm, FuncionarioForm, CursoForm, ReclamacaoForm, Orientador_TeseForm, TemasForm, MatriculaForm,
    Disciplina_Curso_Form, Listar_Estudante_MatriculaForm, Listar_Disciplinas_CadaCurso_Form, Lancamento_nota_Form, DisciplinaForm)

# Biblioteca
from biblioteca.models import Livro, Solicitacao
from biblioteca.forms import Livro_Form, Solicitacao_Obra_Form

# Utilizador
from utilizador.models import Utilizador_User
from utilizador.forms import  Utilizador_Form, LoginForm

# arquivos

from arquivos.models import Arquivo
from arquivos.forms import Arquivo_Form, ConsultarForm


#INFORMAÇÃO/informacao_forum

from informacao_forum.forms import Consultar_Form

# constante do Rodape das menssagem
SOFIL_WEB = '<a href>SOFIL-WEB</a>'
SENHA_PADRAO = 'kanguitu'
