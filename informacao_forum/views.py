from helper.includes import *
from django.db.models import Q



@login_required
def ver_minha_nota(request):
    form =Consultar_Form(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            try:
                curso = request.POST.get('curso')
                aluno = form.cleaned_data.get('aluno')
                lista = Nota.objects.select_related('aluno').filter(aluno_id=aluno, curso_id=curso)
                dados = lista.first()
                context = {'lista': lista, 'resp': dados}
                return render (request, 'informacao_forum/perfil_estudante.html', context)
            except Exception as e:
                print(e)
                sweetify.error(request, 'Dados não Localizado', position ='top-end',   persistent='OK', timer='4100')
    context = {'form': form}
    return render (request, 'informacao_forum/ver_minha_nota.html', context)


# ZONA ONDE É FEITO OS PEDIDOS DE LISTAGEM DE DADOS
@login_required
def listar_solicitacao_tema_proposta(request):
    lista = Tema.objects.select_related().filter(Q(situacao__startswith='Proposta-Aprovada') | Q(situacao__startswith='Proposta'))
    context = {'lista': lista}
    return render (request, 'secretaria/listar_tema_proposta.html', context)


@login_required
def listar_temas_tese(request):
    lista = Tema.objects.select_related('curso').filter(situacao='Aprovado').all().order_by('-curso')
    context = {'lista': lista}
    return render (request, 'secretaria/listar_temas_tese.html', context)


@login_required
def listar_reclamacao(request):
    lista =  Reclamacao.objects.select_related('aluno').all().order_by('-aluno')
    context = {'lista': lista}
    return render (request, 'secretaria/listar_reclamacao.html', context)


@login_required
def listar_professor_orientador(request):
    #sweetify.success(request,'Seja bem vindo!...', button='Ok', timer='3200', persistent='OK', footer='<a href>SOFIL-WEB</a>')
    lista = Orientador.objects.select_related('docente').all().order_by('-id')
    context = {'lista':lista}
    return render (request, 'secretaria/listar_professor_orientador.html', context)


# função que vai listar dados do estudante matriculado, em função da escolha
@login_required
def listar_estudante(request):
    form = Listar_Estudante_MatriculaForm(request.POST or None)
    if request.method == "POST":
        curso = request.POST.get('curso')
        opcao_matricula = request.POST.get('opcao_matricula')
        ano_frequencia = request.POST.get('ano_frequencia')
        periodo = request.POST.get('periodo')
        data_final = request.POST.get('data_final')
        data = request.POST.get('data')

        if curso and opcao_matricula and ano_frequencia and periodo and data_final and data:
            lista = Matricula.objects.select_related('aluno').filter(curso_id=curso, opcao_matricula_id=opcao_matricula, ano_frequencia_id=ano_frequencia, periodo=periodo).order_by('-id')
            if data > data_final:
                dados = lista.filter(data__range=(data, data_final))
                context = {'lista':dados}
                return render (request, 'secretaria/listar_estudante.html', context)
            else:
                context = {'lista':lista}
                return render (request, 'secretaria/listar_estudante.html', context)

        elif curso and opcao_matricula and ano_frequencia and periodo and data:
            lista = Matricula.objects.select_related('aluno').filter(curso_id=curso, opcao_matricula_id=opcao_matricula, ano_frequencia_id=ano_frequencia, periodo=periodo).order_by('-id')
            dados = lista.filter(data__contains=data[:-3])
            context = {'lista':dados}
            return render (request, 'secretaria/listar_estudante.html', context)

        elif curso and opcao_matricula and ano_frequencia and periodo and data_final:
            lista = Matricula.objects.select_related('aluno').filter(curso_id=curso, opcao_matricula_id=opcao_matricula, ano_frequencia_id=ano_frequencia, periodo=periodo).order_by('-id')
            dados = lista.filter(data_final__contains=data[:-3])
            context = {'lista':dados}
            return render (request, 'secretaria/listar_estudante.html', context)

        elif curso and opcao_matricula and ano_frequencia and periodo:
            lista = Matricula.objects.select_related('aluno').filter(curso_id=curso, opcao_matricula_id=opcao_matricula, ano_frequencia_id=ano_frequencia, periodo=periodo).order_by('-id')
            context = {'lista':lista}
            return render (request, 'secretaria/listar_estudante.html', context)

        elif curso and opcao_matricula and ano_frequencia:
            lista = Matricula.objects.select_related('aluno').filter(curso_id=curso, opcao_matricula_id=opcao_matricula, ano_frequencia_id=ano_frequencia).order_by('-id')
            context = {'lista':lista}
            return render (request, 'secretaria/listar_estudante.html', context)

        elif curso and opcao_matricula and periodo:
            lista = Matricula.objects.select_related('aluno').filter(curso_id=curso, opcao_matricula_id=opcao_matricula, periodo=periodo).order_by('-id')
            context = {'lista':lista}
            return render (request, 'secretaria/listar_estudante.html', context)

        elif curso and ano_frequencia and periodo:
            lista = Matricula.objects.select_related('aluno').filter(curso_id=curso, ano_frequencia_id=ano_frequencia, periodo=periodo).order_by('-id')
            context = {'lista':lista}
            return render (request, 'secretaria/listar_estudante.html', context)

        elif curso and opcao_matricula:
            lista = Matricula.objects.select_related('aluno').filter(curso_id=curso, opcao_matricula_id=opcao_matricula).order_by('-id')
            context = {'lista':lista}
            return render (request, 'secretaria/listar_estudante.html', context)
        elif curso and ano_frequencia:
            lista = Matricula.objects.select_related('aluno').filter(curso_id=curso, ano_frequencia_id=ano_frequencia).order_by('-id')
            context = {'lista':lista}
            return render (request, 'secretaria/listar_estudante.html', context)
        elif curso and periodo:
            lista = Matricula.objects.select_related('aluno').filter(curso_id=curso, periodo=periodo).order_by('-id')
            context = {'lista':lista}
            return render (request, 'secretaria/listar_estudante.html', context)
        elif curso:
            lista = Matricula.objects.select_related('aluno').filter(curso_id=curso).order_by('-id')
            context = {'lista':lista}
            return render (request, 'secretaria/listar_estudante.html', context)


    context = {'form': form}
    return render (request, 'secretaria/menu_listar_estudante_Matricula.html', context)


@login_required
def listar_cursos(request):
    lista = Curso.objects.all().order_by('id')
    context = {'lista': lista}
    return render (request, 'secretaria/listar_curso.html', context)


# views que vai listar disciplina cadastrada no sistema
@login_required
def listar_disciplinas(request):
    lista = Disciplinas.objects.all().order_by('id')
    context = {'lista':lista}
    return render (request, 'secretaria/listar_disciplina.html', context)


# views que vai listar as disciplina de cada curso, em função da escolha
@login_required
def listar_disciplinas_cada_curso(request):
    form = Listar_Disciplinas_CadaCurso_Form(request.POST or None)
    if request.method == "POST":
        curso = request.POST.get('curso')
        lista = Disciplina_Curso.objects.select_related('curso').filter(curso_id=curso).order_by('-id')
        resp = Curso.objects.get(id=curso)
        context = {'lista':lista, 'curso':resp}
        return render (request, 'secretaria/listar_disciplinas_cada_curso.html', context)
    context = {'form':form}
    return render (request, 'secretaria/menu_disciplinas_cada_curso.html', context)
