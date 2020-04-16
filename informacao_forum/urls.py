from django.urls import path
from . import views
from hashlib import blake2b

app_name = 'informacao_forum'
urlpatterns = [
    path(blake2b(b'listar_estudante').hexdigest()+'/', views.listar_estudante, name='lista-estudante'),
    path(blake2b(b'listar_cursos').hexdigest()+'/', views.listar_cursos, name='lista-curso'),
    path(blake2b(b'listar_disciplinas').hexdigest()+'/', views.listar_disciplinas, name='lista-disciplina'),
    path(blake2b(b'listar_reclamacao').hexdigest()+'/', views.listar_reclamacao, name='listar-reclamacao'),
    path(blake2b(b'listar_professor_orientador').hexdigest()+'/', views.listar_professor_orientador, name='listar-orientador'),
    path(blake2b(b'listar_temas_tese').hexdigest()+'/', views.listar_temas_tese, name='listar-tema'),
    path(blake2b(b'listar_tema_proposta').hexdigest()+'/', views.listar_solicitacao_tema_proposta, name='listar-proposta'),
    path(blake2b(b'listar_disciplinas_cada_curso').hexdigest()+'/', views.listar_disciplinas_cada_curso, name='disciplinas-cada-curso'),
    path(blake2b(b'ver_minha_nota').hexdigest()+'/', views.ver_minha_nota, name='ver-minha-nota'),


]
