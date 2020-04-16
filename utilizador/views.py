#from django.shortcuts import render
from helper.includes import *

# Create your views here.


@login_required
def listar_utilizador(request):
    lista = Utilizador_User.objects.select_related('user').all().order_by('-id')
    context = {'lista':lista}
    return render (request, 'utilizador/listar_utilizador.html', context)


@login_required
def eliminar_conta(request, pk):
    if pk > 0:
        user = User.objects.filter(id=pk).delete()
        sweetify.success(request,'Conta Eliminada com sucesso!....', timer='4900', button='Ok', footer=SOFIL_WEB)
        return HttpResponseRedirect(reverse('utilizador:listar'))
    else:
        sweetify.info(request,'Acesso Negado!Falha....', timer='4900', button='Ok', footer=SOFIL_WEB)
        return HttpResponseRedirect(reverse('utilizador:listar'))

@login_required
def desativar_conta(request, pk):
    if pk > 0:
        user = User.objects.get(id=pk)
        user.is_active = 0
        user.save()
        sweetify.success(request,'Conta Desativada com sucesso!....', timer='4900', button='Ok', footer=SOFIL_WEB)
        return HttpResponseRedirect(reverse('utilizador:listar'))
    else:
        sweetify.info(request,'Acesso Negado!Falha....', timer='4900', button='Ok', footer=SOFIL_WEB)
        return HttpResponseRedirect(reverse('utilizador:listar'))

@login_required
def ativar_conta(request, pk):
    if pk > 0:
        user = User.objects.get(id=pk)
        user.is_active = 1
        user.save()
        sweetify.success(request,'Conta Ativado com sucesso!....', timer='4900', button='Ok', footer=SOFIL_WEB)
        return HttpResponseRedirect(reverse('utilizador:listar'))
    else:
        sweetify.info(request,'Acesso Negado!Falha....', timer='4900', button='Ok', footer=SOFIL_WEB)
        return HttpResponseRedirect(reverse('utilizador:listar'))


@login_required
def alterar_senha(request):
    if request.POST == "POST":
        pass



def login_utilizador(request):
    form =LoginForm(request.POST or None)
    if request.method == 'POST':
        try:
            if form.is_valid():
                senha = form.cleaned_data.get('senha')
                nome = form.cleaned_data.get('nome_utilizador')
                user = authenticate(username=nome,password=senha)
                if user is not None:
                    if user.is_active:
                        login(request, user)
                        return HttpResponseRedirect(reverse('secretaria:home'))
                    else:
                        sweetify.info(request, 'A Conta esta desativada <br> Diriga-se ao Administrador!.', persistent='OK')
                        return HttpResponseRedirect(reverse('utilizador:sair'))
                else:
                    messages.warning(request, 'Dados errados!...')
        except User.DoesNotExist:
            messages.warning(request, 'A conta não existe...')

    context = {'form': form}
    return render (request, 'homes/login.html', context)


@login_required
def criar_conta_utilizador(request):
    form = Utilizador_Form(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            nome =form.cleaned_data.get('nome_utilizador')
            categoria =form.cleaned_data.get('categoria')
            id =form.cleaned_data.get('bi')
            user = User.objects.create_user(username=nome,last_name=categoria,password=SENHA_PADRAO)
            resp = Utilizador_User.objects.create(pessoa_id=id, user_id=user.id)
            resp.save()
            sweetify.success(request,'Conta criada com sucesso!....', timer='4900', button='Ok', footer=SOFIL_WEB)
            return HttpResponseRedirect(reverse('secretaria:home-kanguitu'))

    context = {'form': form}
    return render (request, 'utilizador/criar_conta.html', context)

@login_required
def sair(request):
    try:
        #del request.session['salakiaku']
        logout(request)
        return HttpResponseRedirect(reverse('utilizador:login-home'))
    except Exception as e:
        raise Http404("erro a terminar a sessão %s " % (e))
