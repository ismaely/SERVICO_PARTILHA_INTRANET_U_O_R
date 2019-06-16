
from helper.includes import *
#from django.views.generic import ListView, DeleteView, DetailView


class Home_View(generic.ListView):

    template_name = 'homes/home.html'
    def get_queryset(self):
        #sweetify.success(request,'Seja bem vindo!....', button='Ok', timer='3200')
        return None



def login(request):
    context = {}
    return render (request, 'homes/login.html', context)



def registar_nota_aluno(request):
    context = {}
    return render (request, 'secretaria/registar_nota_aluno.html', context)



def registar_cursos(request):
    context = {}
    return render (request, 'secretaria/registar_cursos.html', context)



def registar_disciplina(request):
    context = {}
    return render (request, 'secretaria/registar_disciplina.html', context)



def registar_professor_orientarTese(request):
    context = {}
    return render (request, 'secretaria/registar_professor_orientador.html', context)



def registar_tema_monografia(request):
    context = {}
    return render (request, 'secretaria/registar_tema_monografia.html', context)



def registar_solicitacao_tema_monografia(request):
    context = {}
    return render (request, 'secretaria/registar_solicitacao_tema_monografia.html', context)



def registar_reclamacao(request):
    context = {}
    return render (request, 'secretaria/registar_reclamacao.html', context)


def registar_trabalho_fim_curso(request):
    context = {}
    return render (request, 'secretaria/registar_trabalho_fim_curso.html', context)


def registar_defesa_final_curso_aluno(request):
    context = {}
    return render (request, 'secretaria/registar_defesa_final_curso.html', context)



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
            sweetify.success(request, 'Dados Registado com sucesso!....', button='Ok', timer='3100')
            return HttpResponseRedirect(reverse('secretaria:home-kanguitu'))
    #print(form3.errors)
    #print(form4.errors)
    context = {'form': form, 'form2': form2, 'form3': form3, 'form4': form4}
    #sweetify.success(request,'Seja bem vindo!....', button='Ok', timer='3200')
    template = 'secretaria/registar_cadastro.html'
    return render(request, template, context)



@csrf_exempt
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
