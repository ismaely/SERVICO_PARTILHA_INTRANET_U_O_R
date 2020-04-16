from helper.includes import *

# Create your views here.

@login_required
def visualizar_arquivo(request, pk):
    resp = Arquivo.objects.get(id=pk)
    context = {'lista': resp}
    return render (request, 'arquivos/visualizar_arquivo.html', context)


@login_required
def listar_arquivos(request):
    lista = Arquivo.objects.select_related().all().order_by('-titulo')
    context = {'lista':lista}
    return render (request, 'arquivos/listar_arquivos.html', context)


@login_required
def eliminar_arquivos(request, pk):
    if pk > 0:
        lista = Arquivo.objects.get(id=pk).delete()
        sweetify.success(request,'Dados eliminado comsucesso!....', timer='4900', button='Ok', footer=SOFIL_WEB)
        #return HttpResponseRedirect(reverse('secretaria:listar-modulos-mestrado'))
        return HttpResponseRedirect(reverse('arquivo:listar-arquivos'))


@login_required
def procura_arquivos(request):
    form = ConsultarForm(request.POST or None)
    if request.method == "POST":
        nome = request.POST['nome'].upper()
        lista = Arquivo.objects.filter(Q(titulo__contains=nome) | Q(autor__contains=nome))
        context = {'lista': lista}
        return render (request, 'arquivos/listar_arquivos.html', context)

    context = {'form': form}
    return render (request, 'arquivos/procura_arquivos.html', context)


@login_required
#FUNÇÃO QUE VAI ATUALIZAR OS DADOS DE UM ARQUIVO
def atualizar_arquivos(request, pk):
    resp = Arquivo.objects.get(id=pk)
    form = Arquivo_Form(request.POST or None, instance=resp)
    if request.method == "POST":
        form = Arquivo_Form(request.POST, request.FILES, instance=resp)
        if form.is_valid():
            form.save()
            sweetify.success(request,'Arquivo Atualizado com sucesso!....', timer='4900', button='Ok', footer=SOFIL_WEB)
            return HttpResponseRedirect(reverse('arquivo:listar-arquivos'))
    #print(form.errors)
    context = {'form': form, 'pk': resp.id }
    return render (request, 'arquivos/registar_arquivos.html', context)


@login_required
def registar_arquivos(request):
    form = Arquivo_Form(request.POST or None)
    if request.method == "POST":
        form = Arquivo_Form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            sweetify.success(request,'Arquivo Registado com sucesso!....', timer='4900', button='Ok', footer=SOFIL_WEB)
            return HttpResponseRedirect(reverse('secretaria:home'))
    #print(form.errors)
    context = {'form': form}
    return render (request, 'arquivos/registar_arquivos.html', context)
