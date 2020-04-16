
from helper.includes import *
from django.db.models import Q
#from django.views.generic import ListView, DeleteView, DetailView




class Home_View(generic.ListView):
    template_name = 'homes/home.html'
    def get_queryset(self):
        return None


#@login_required
def editar_estudante_matriculado(request, pk):
    resp = Matricula.objects.get(id=pk)
    form = MatriculaForm(request.POST or None,instance=resp, initial={'aluno': resp.aluno.pessoa.bi}) #, initial={'estudante': resp.estudante.pessoa.bi}
    if request.method == 'POST':
        if form.is_valid():
            resp = form.save(commit=False)
            resp.aluno_id = form.cleaned_data.get('aluno')
            resp.save()

            sweetify.success(request,'Dados Alterado com sucesso sucesso!....', timer='4900', button='Ok', footer=SOFIL_WEB)
            return render (request, 'secretaria/sucesso_imprimir_ficha_matricula.html', {'id': resp.id})
    context = {'form': form, 'edita': pk}
    return render (request, 'secretaria/registar_matricula.html', context)


#RECEBE O ID DO CURSO E ANO RETORNA TODOS AS DISCIPLINA
def recebe_id_curso_ajax(request):
    try:
        dados = dict()
        if request.method == 'POST':
            valor = []
            valor = request.body.decode('utf-8')
            valor = json.loads(valor)
            curso = valor['curso']
            ano = valor['ano']
            semestre = valor['semestre']
            lista = [(k.disciplina.id, k.disciplina.nome)for k in Disciplina_Curso.objects.select_related('curso').filter(curso_id=curso, ano_id= ano, semestre_id=semestre).all()]
            dados = {
                'resposta':  lista
            }
        return JsonResponse(dados)
    except ValueError:
        print("ERRO NO CURSO PARA NOTA ")



@login_required
def aprovar_proposta_tema(request, pk):
    try:
        resp = Tema.objects.get(id=pk)
        resp.situacao = 'Proposta-Aprovada'
        resp.save()
    except Tema.DoesNotExist:
        sweetify.error(request,'O Erro não foi possivel!....', timer='4900', persistent='OK', footer=SOFIL_WEB)
    return HttpResponseRedirect(reverse('secretaria:listar-proposta'))


#----- ZONA OND É FEITO TODOS TIPO DE CADASTRO OU ADICIONAR QUE VEM DO FORMULARIO

@login_required
def registar_nota_aluno(request):
    form =Lancamento_nota_Form(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            try:
                curso = int(request.POST.get('curso'))
                disciplina = int(request.POST.get('disciplina'))
                aluno = form.cleaned_data.get('aluno')
                ano = form.cleaned_data.get('ano')
                nota = form.cleaned_data.get('nota')
                semestre = form.cleaned_data.get('semestre')

                matricula = Matricula.objects.select_related('curso').get(aluno_id=aluno, curso_id= curso, ano__nome=ano, semestre__nome=semestre)
                if matricula.ano.nome == str(ano) and matricula.curso_id == curso and matricula.aluno_id ==aluno:
                    try:
                        dados = Nota.objects.select_related('curso').get(aluno_id=aluno, disciplina_id=disciplina, curso_id=curso)
                        if dados.nota is not None:
                            sweetify.error(request, 'O estudante já tem Nota nesta cadeira! <br> Contacta o Admin!..', position ='top-end',persistent='OK', timer='3100')
                        descricao = Descricao_Nota.objects.get(valor=nota)
                        resp = form.save(commit=False)
                        resp.aluno_id = aluno
                        resp.curso_id = curso
                        resp.descricao_id = descricao.id
                        resp.disciplina_id = disciplina
                        resp.save()
                        sweetify.success(request, 'Inserido com Sucesso!..',position ='top-end', button='Ok', timer='4100')
                    except Exception as e:
                        raise

                else:
                    sweetify.error(request, 'Não pode ser lançada a nota porque; não fez a inscrição', position ='top-end',   persistent='OK', timer='4100')
            except Exception as e:
                print(e)
                sweetify.error(request, 'Não pode ser lançada!! não esta inscrito', position ='top-end',   persistent='OK')

    context = {'form':form}
    return render (request, 'secretaria/registar_nota_aluno.html', context)


@login_required
def registar_entrada_trabalho_fim_curso(request):
    context = {}
    return render (request, 'secretaria/registar_trabalho_fim_curso.html', context)


@login_required
def registar_defesa_final_curso_aluno(request):
    context = {}
    return render (request, 'secretaria/registar_defesa_final_curso.html', context)


@login_required
def registar_matricula(request):
    form = MatriculaForm(request.POST or None)
    if request.method == "POST":
        #id = helper.core.retorna_id(request)
        if form.is_valid():
            resp = form.save(commit=False)
            resp.aluno_id = form.cleaned_data.get('aluno')
            resp.save()
            sweetify.success(request,'Matricula registada com sucesso!....', timer='4900', button='Ok', footer=SOFIL_WEB)
            return render (request, 'secretaria/sucesso_imprimir_ficha_matricula.html', {'id': resp.id})

    context = {'form': form}
    return render (request, 'secretaria/registar_matricula.html', context)


@login_required
def registar_solicitacao_tema_monografia(request):
    form = TemasForm(request.POST or None)
    if request.method == "POST":
        id = helper.core.retorna_id(request)
        if form.is_valid() and id > 0:
            resp = form.save(commit=False)
            resp.aluno_id = id
            resp.situacao = "Proposta"
            resp.save()
            sweetify.success(request,'Solicitação do tema enviado com sucesso!....', timer='4900', button='Ok', footer=SOFIL_WEB)
            return HttpResponseRedirect(reverse('secretaria:home'))

    context = {'form': form}
    return render (request, 'secretaria/registar_solicitacao_tema_monografia.html', context)


@login_required
def registar_cursos(request):
    form = CursoForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            curso = form.save()
            sweetify.success(request,'Curso Registado com sucesso!....', timer='4900', button='Ok', footer=SOFIL_WEB)
            return HttpResponseRedirect(reverse('secretaria:home'))

    context = {'form': form}
    return render (request, 'secretaria/registar_cursos.html', context)


@login_required
def adicioar_disciplina_curso(request):
    form = Disciplina_Curso_Form(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            curso = form.save()
            sweetify.success(request,'Adicionada com sucesso!....', timer='4900', button='Ok', footer=SOFIL_WEB)
            return render (request, 'secretaria/adicionar_disciplina_curso.html', {'form': form})
            #return HttpResponseRedirect(reverse('secretaria:home'))

    context = {'form': form}
    return render (request, 'secretaria/adicionar_disciplina_curso.html', context)


@login_required
def registar_disciplina(request):
    form = DisciplinaForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            curso = form.save()
            sweetify.success(request,'Disciplina cadastrado com sucesso!....', timer='4900', button='Ok', footer=SOFIL_WEB)
            return HttpResponseRedirect(reverse('secretaria:home'))

    context = {'form': form}
    return render (request, 'secretaria/registar_disciplina.html', context)



def registar_professor_orientarTese(request):
    form = Orientador_TeseForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            curso = form.save()
            sweetify.success(request,'Orientador cadastrado com sucesso!....', timer='4900', button='Ok', footer=SOFIL_WEB)
            return HttpResponseRedirect(reverse('secretaria:home'))

    context = {'form': form}
    return render (request, 'secretaria/registar_professor_orientador.html', context)


@login_required
def registar_tema_monografia(request):
    form = TemasForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            curso = form.save()
            sweetify.success(request,'Tema cadastrado com sucesso!....', timer='4900', button='Ok', footer=SOFIL_WEB)
            return HttpResponseRedirect(reverse('secretaria:home'))

    context = {'form': form}
    return render (request, 'secretaria/registar_tema_monografia.html', context)


@login_required
def registar_reclamacao(request):
    form = ReclamacaoForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            curso = form.save()
            sweetify.success(request,'Reclamação feita com sucesso!....', button='Ok', timer='4900', footer=SOFIL_WEB)
            return HttpResponseRedirect(reverse('secretaria:home'))

    context = {'form': form}
    return render (request, 'secretaria/registar_reclamacao.html', context)


@login_required
def Registar_cadastro(request):
    form = PessoaForm(request.POST or None)
    form2 = DocenteForm(request.POST or None)
    form3 = AlunoForm(request.POST or None)
    form4 = FuncionarioForm(request.POST or None)
    if request.method == "POST":
        form = PessoaForm(request.POST, request.FILES or None)
        if form.is_valid() and form2.is_valid() and form3.is_valid() and form4.is_valid():
            pessoa = form.save()
            if request.POST['categoria'] == 'DOCENTE':
                docente = form2.save(commit=False)
                docente.pessoa_id = pessoa.id
                docente.save()
            if request.POST['categoria'] == 'ESTUDANTE':
                estudante = form3.save(commit=False)
                estudante.pessoa_id = pessoa.id
                estudante.save()
            if request.POST['categoria'] == 'FUNCIONARIO':
                funcionario = form4.save(commit=False)
                funcionario.pessoa_id = pessoa.id
                funcionario.save()
            # prepara a foto para ser guardada
            if request.POST['foto'] is not None:
                foto = helper.core.prepara_foto(request)
                pessoa_foto = Pessoa.objects.get(id=pessoa.id)
                pessoa_foto.foto = foto
                pessoa_foto.save()
            sweetify.success(request,'Dados cadastrado com sucesso!....', button='Ok', timer='4900', footer=SOFIL_WEB)
            return HttpResponseRedirect(reverse('secretaria:home'))
    #print(form3.errors)
    #print(form4.errors)
    context = {'form': form, 'form2': form2, 'form3': form3, 'form4': form4}
    template = 'secretaria/registar_cadastro.html'
    return render(request, template, context)



#função que vai gerar a ficha de matatricula quando a matricula acabar
@login_required
def imprimir_ficha_matricula(request, pk):
    resp = Matricula.objects.select_related('curso').get(id=pk)
    buffer = BytesIO()
    response = HttpResponse(content_type='application/pdf')
    #response['Content-Disposition'] = 'inline; filename="Declaração_pessoal.pdf"'
    doc = SimpleDocTemplate(buffer,pagesize=letter, alignment=TA_JUSTIFY, rightMargin=38,leftMargin=70,topMargin=135,bottomMargin=75)
    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(name='Justify',  alignment=TA_JUSTIFY, fontSize=12.5, fontName="Times-Roman"))
    centro = ParagraphStyle(name='medio', leading = 15, fontName="Times-Roman")
    estilo_linha = ParagraphStyle(name='medio', leading = 10, fontName="Times-Roman")

    #print(request.user)
    Story = []
    TABELA = []
    DADOS = []
    DADOS_2 = []
    DADOS_3 = []
    CADEIRAS = []
    ano = []
    ano = str(resp.data).split('-')
    ptext = """<font size=13.5>  Recibo Nº:  <br/> Confirmação de Matrícula
    <br/> %s <br/> Ano Lectivo: %s</font>"""
    ptext = ptext % (resp.curso.nome, ano[0])
    #centro.rightIndent = 27
    centro.leftIndent = 6 * cm
    Story.append(Paragraph(ptext, centro))

    # A LINHA PRETA
    linha = '______'
    for lin in range(3):
        linha += linha
    ptext = """<font size=20.5>  <b> %s </b> </font>"""
    ptext = ptext % (linha)
    Story.append(Paragraph(ptext, estilo_linha))

    Story.append(Spacer(1, 2* cm))
    # tabela 1ª
    LEGENDA = ['NOME', 'Nº ESTUDANTE']
    DADOS.append([str(resp.aluno.pessoa.nome).upper(), str(resp.aluno.numero_estudante).upper()])
    TABELA = Table([LEGENDA] + DADOS,colWidths=[13.3 * cm, 4.8 * cm, 1.0 * cm, 1.0 * cm])
    TABELA.setStyle(TableStyle([
        ('GRID', (0, 0), (6, -1), 1.3,  colors.black),
        ('LINEBELOW', (0, 0), (-1, 0), 1.3, colors.black),
        ('BACKGROUND', (0, 0), (-1, 0), colors.lightblue)
        ]))
    Story.append(TABELA)

    # segunda tabela
    LEGENDA = ['B.I. Nº', 'GÉNERO']
    DADOS_2.append([str(resp.aluno.pessoa.bi).upper(), str(resp.aluno.pessoa.genero).upper()])
    TABELA = Table([LEGENDA] + DADOS_2,colWidths=[13.3 * cm, 4.8 * cm, 1.0 * cm, 1.0 * cm])
    TABELA.setStyle(TableStyle([
        ('GRID', (0, 0), (6, -1), 1.3,  colors.black),
        ('LINEBELOW', (0, 0), (-1, 0), 1.3, colors.black),
        ('BACKGROUND', (0, 0), (-1, 0), colors.lightblue)
        ]))
    Story.append(TABELA)
    Story.append(Spacer(1, 14.5))

    # 3ª TABELA DAS DISCIPLINA
    LEGENDA = ['DISCIPLINA',  'ANO', 'SEMESTRE']
    for modul in Disciplina_Curso.objects.select_related('curso').filter(curso_id=resp.curso_id, ano_id=resp.ano_id).all():
        DADOS_3.append([str(modul.disciplina.nome),str( modul.ano.nome), str( modul.semestre.nome)])

    TABELA = Table([LEGENDA] + DADOS_3,colWidths=[12.3 * cm, 2.5 * cm, 3.3 * cm, 1.0 * cm])
    TABELA.setStyle(TableStyle([
        ('GRID', (0, 0), (6, -1), 1.3,  colors.black),
        ('LINEBELOW', (0, 0), (-1, 0), 1.3, colors.black),
        ('BACKGROUND', (0, 0), (-1, 0), colors.lightblue)
        ]))
    Story.append(TABELA)


    # DATA DA CRIAÇÃO DA DECLARAÇÃO
    Story.append(Spacer(1, 3.5))
    DATAS = date.today()
    ptext = 'Luanda aos %s de %s de %s'
    ptext = ptext % (DATAS.day, MESES[DATAS.month - 1], DATAS.year)
    #Story.append(Paragraph(ptext, paragrafo_data))

    response['Content-Disposition'] = 'inline; filename=FICHA.pdf' # NOME DO FICHEIRO
    Story.append(PageBreak())
    doc.build(Story, onFirstPage=helper.core.rodape_ficha_matricula)
    response.write(buffer.getvalue())
    buffer.close()
    return response



#@csrf_exempt
def retorna_municipio(request):
    if request.method == 'POST':
        dados = dict()
        cod = []
        cod = request.body.decode('utf-8')
        lista = json.loads(cod)
        if lista['provincia'] == 'Luanda':
            dados = {
                'dados': LUANDA,
            }
            return JsonResponse(dados)
        elif lista['provincia'] == 'Bengo':
            dados = {
                'dados': BENGO,
            }
            return JsonResponse(dados)
        elif lista['provincia'] == 'Benguela':
            dados = {
                'dados': BENGUELA,
            }
            return JsonResponse(dados)
        elif lista['provincia'] == 'Bié':
            dados = {
                'dados': BIE,
            }
            return JsonResponse(dados)
        elif lista['provincia'] == 'Cabinda':
            dados = {
                'dados': CABINDA,
            }
            return JsonResponse(dados)
        elif lista['provincia'] == 'Cabinda':
            dados = {
                'dados': CABINDA,
            }
            return JsonResponse(dados)
        elif lista['provincia'] == 'Cunene':
            dados = {
                'dados': CUNENE,
            }
            return JsonResponse(dados)
        elif lista['provincia'] == 'Huambo':
            dados = {
                'dados': HUAMBO,
            }
            return JsonResponse(dados)
        elif lista['provincia'] == 'Huila':
            dados = {
                'dados': HUILA,
            }
            return JsonResponse(dados)
        elif lista['provincia'] == 'Cuando Cubango':
            dados = {
                'dados': CUANDO_CUBANGO,
            }
            return JsonResponse(dados)
        elif lista['provincia'] == 'Cuanza Norte':
            dados = {
                'dados': CUANZA_NORTE,
            }
            return JsonResponse(dados)
        elif lista['provincia'] == 'Cuanza Sul':
            dados = {
                'dados': CUANZA_SUL,
            }
            return JsonResponse(dados)
        elif lista['provincia'] == 'Lunda Norte':
            dados = {
                'dados': LUNDA_NORTE,
            }
            return JsonResponse(dados)
        elif lista['provincia'] == 'Lunda Sul':
            dados = {
                'dados': LUNDA_SUL,
            }
            return JsonResponse(dados)
        elif lista['provincia'] == 'Malanje':
            dados = {
                'dados': MALANJE,
            }
            return JsonResponse(dados)
        elif lista['provincia'] == 'Moxico':
            dados = {
                'dados': MOXICO,
            }
            return JsonResponse(dados)
        elif lista['provincia'] == 'Namibe':
            dados = {
                'dados': NAMIBE,
            }
            return JsonResponse(dados)
        elif lista['provincia'] == 'Uige':
            dados = {
                'dados': UIGE,
            }
            return JsonResponse(dados)
        elif lista['provincia'] == 'Zaire':
            dados = {
                'dados': ZAIRE,
            }
            return JsonResponse(dados)
