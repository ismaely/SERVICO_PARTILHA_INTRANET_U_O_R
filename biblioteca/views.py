from helper.includes import *

# Create your views here.


@login_required
def eliminar_obra(request, pk):
    if pk > 0:
        lista = Livro.objects.get(id=pk).delete()
        sweetify.success(request,'Dados eliminado com sucesso!....', timer='4900', button='Ok', footer=SOFIL_WEB)
        #return HttpResponseRedirect(reverse('secretaria:listar-modulos-mestrado'))
        return HttpResponseRedirect(reverse('secretaria:listar-obras'))


# FUNÇÃO QUE VAI ATIVAR A SOLICIATAÇÃO
@login_required
def ativar_solicitacao_obra(request, pk):
    if pk > 0:
        resp = Solicitacao.objects.get(id=pk)
        resp.estado = "Aprovado"
        resp.save()
        sweetify.success(request, 'Solicitação Aprovado com sucesso',  timer='4900', button='Ok', footer=SOFIL_WEB)
    return HttpResponseRedirect(reverse('biblioteca:listar-solicitacao'))


@login_required
def cancelar_solicitacao_obra(request, pk):
    if pk > 0:
        resp = Solicitacao.objects.get(id=pk)
        resp.estado = "Cancelar"
        resp.save()
        sweetify.success(request, 'Solicitação Cancelada', timer='4900', button='Ok', footer=SOFIL_WEB)
    return HttpResponseRedirect(reverse('biblioteca:listar-solicitacao'))



@login_required
# função que vai efetuar a consulta dos dads quando for solicitado pela routa
def efectuar_consulta(request):
    form = ConsultarForm(request.POST or None)
    if request.method == "POST":
        nome = request.POST['nome'].lower()
        lista = Livro.objects.filter(Q(titulo__contains=nome) | Q(autor__contains=nome))
        context = {'lista': lista}
        return render (request, 'biblioteca/listar_livros.html', context)

    context = {'form': form}
    return render (request, 'biblioteca/consultar.html', context)


@login_required
def listar_obras(request):
    lista = Livro.objects.select_related('nome').all().order_by('-titulo')
    context = {'lista':lista}
    return render (request, 'biblioteca/listar_livros.html', context)


@login_required
def listar_solicitacao(request):
    #sweetify.success(request,'Seja bem vindo!....', button='Ok', timer='3200', persistent='OK', footer='<a href>SOFIL-WEB</a>')
    lista = Solicitacao.objects.select_related('aluno').all().order_by('-titulo')
    context = {'lista':lista}
    return render (request, 'biblioteca/listar_solicitacao.html', context)


@login_required
def atualizar_obra_literaria(request, pk):
    resp = Livro.objects.get(id=pk)
    form = Livro_Form(request.POST or None, instance=resp)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            sweetify.success(request,'Dados atualizado com sucesso!....', timer='4900', button='Ok', footer=SOFIL_WEB)
            return HttpResponseRedirect(reverse('biblioteca:listar-obras'))
    #print(form.errors)
    context = {'form': form, 'pk': resp.id}
    return render (request, 'biblioteca/cadastrar_livro.html', context)


@login_required
def atualizar_obra_solicitada(request, pk):
    resp = Solicitacao.objects.get(id=pk)
    form = Solicitacao_Obra_Form(request.POST or None, instance=resp, initial={'aluno': resp.aluno.pessoa.bi})
    if request.method == "POST":
        if form.is_valid():
            aluno = form.cleaned_data.get('aluno')
            fro = form.save(commit=False)
            fro.aluno_id = aluno
            fro.save()
            sweetify.success(request,'Solicitação atualizada  com sucesso!....', timer='4900', button='Ok', footer=SOFIL_WEB)
            return HttpResponseRedirect(reverse('biblioteca:listar-solicitacao'))
    context = {'form': form, 'pk': pk}
    return render (request, 'biblioteca/registar_solicitacao_obra.html', context)



@login_required
def cadastrar_obra_literaria(request):
    form = Livro_Form(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            sweetify.success(request,'Cadastro com sucesso!....', timer='4900', button='Ok', footer=SOFIL_WEB)
            return HttpResponseRedirect(reverse('secretaria:home'))
    #print(form.errors)
    context = {'form': form}
    return render (request, 'biblioteca/cadastrar_livro.html', context)



@login_required
def rgistar_solicitacao_obra(request):
    form = Solicitacao_Obra_Form(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            aluno = form.cleaned_data.get('aluno')
            fro = form.save(commit=False)
            fro.aluno_id = aluno
            fro.save()
            sweetify.success(request,'Solicitação efectuada com sucesso!....', timer='4900', button='Ok', footer=SOFIL_WEB)
            return HttpResponseRedirect(reverse('secretaria:home'))
    #print(form.errors)
    context = {'form': form}
    return render (request, 'biblioteca/registar_solicitacao_obra.html', context)
