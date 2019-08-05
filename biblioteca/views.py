from helper.includes import *

# Create your views here.



def listar_livros(request):
    #sweetify.success(request,'Seja bem vindo!....', button='Ok', timer='3200', persistent='OK', footer='<a href>SOFIL-WEB</a>')
    lista = Livro.objects.select_related('nome').all().order_by('-titulo')
    context = {'lista':lista}
    return render (request, 'biblioteca/listar_livros.html', context)



def cadastrar_livro(request):
    form = Livro_Form(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            sweetify.success(request,'Cadastro com sucesso!....', timer='4900', button='Ok', footer=SOFIL_WEB)
            return HttpResponseRedirect(reverse('secretaria:home-kanguitu'))
    print(form.errors)
    context = {'form': form}
    return render (request, 'biblioteca/cadastrar_livro.html', context)
