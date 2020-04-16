from django.urls import path
from hashlib import blake2b
from . import views



app_name = 'biblioteca'
urlpatterns = [
    path(blake2b(b'cadastrar_obra_literaria').hexdigest()+'/', views.cadastrar_obra_literaria, name='cadastrar-obra'),
    path(blake2b(b'listar_obras').hexdigest()+'/', views.listar_obras, name='listar-obras'),
    path(blake2b(b'registar_solicitacao_obra').hexdigest()+'/', views.rgistar_solicitacao_obra, name='solicitacao_obra'),
    path(blake2b(b'listar_solicitacao').hexdigest()+'/', views.listar_solicitacao, name='listar-solicitacao'),
    path(blake2b(b'consultar_obra').hexdigest()+'/', views.efectuar_consulta, name='consultar'),
    path(blake2b(b'atualizar_obra_literaria').hexdigest()+'/<int:pk>/', views.atualizar_obra_literaria, name='atualizar-obra'),
    path(blake2b(b'eliminar_obra').hexdigest()+'/<int:pk>/', views.eliminar_obra, name='eliminar-obra'),
    path(blake2b(b'atualizar_obra_solicitada').hexdigest()+'/<int:pk>/', views.atualizar_obra_solicitada, name='atualizar-obra-solicitada'),
    path(blake2b(b'ativar_solicitacao_obra').hexdigest()+'/<int:pk>/', views.ativar_solicitacao_obra, name='ativar-solicitacao-obra'),
    path(blake2b(b'cancelar_solicitacao_obra').hexdigest()+'/<int:pk>/', views.cancelar_solicitacao_obra, name='cancelar-solicitacao'),

]
