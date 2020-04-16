from django.urls import path
from hashlib import blake2b
from . import views

app_name = 'secretaria'
urlpatterns = [
    #path('', views.Home_View.as_view(), name='home'),
    path(blake2b(b'home').hexdigest()+'/', views.Home_View.as_view(), name='home'),
    path(blake2b(b'registar_cadastro').hexdigest()+'/', views.Registar_cadastro, name='registar-cadastro'),
    path(blake2b(b'municipio_retorna').hexdigest()+'/', views.retorna_municipio, name='municipio-retorna'),
    path(blake2b(b'registar_orientador_tese').hexdigest()+'/', views.registar_professor_orientarTese, name='registar-orientador-tese'),
    path(blake2b(b'registar_tema_monografia').hexdigest()+'/', views.registar_tema_monografia, name='registar-tema-monografia'),
    path(blake2b(b'registar_solicitacao_tema_monografia').hexdigest()+'/', views.registar_solicitacao_tema_monografia, name='registar-solicitacao-monografia'),
    path(blake2b(b'registar_reclamacao').hexdigest()+'/', views.registar_reclamacao, name='registar-reclamacao'),
    path(blake2b(b'registar_trabalho_fim_curso').hexdigest()+'/', views.registar_entrada_trabalho_fim_curso, name='registar-trabalho-fim_curso'),
    path(blake2b(b'registar_defesa_final_curso_aluno').hexdigest()+'/', views.registar_defesa_final_curso_aluno, name='registar-defesa-final'),
    path(blake2b(b'registar_nota_aluno').hexdigest()+'/', views.registar_nota_aluno, name='registar-nota-aluno'),
    path(blake2b(b'registar_curso').hexdigest()+'/', views.registar_cursos, name='registar-cursos'),
    path(blake2b(b'registar_disciplina').hexdigest()+'/', views.registar_disciplina, name='registar-disciplina'),
    path(blake2b(b'aprovar_proposta_tema').hexdigest()+'/<int:pk>/', views.aprovar_proposta_tema, name='aprovar-proposta-tema'),
    path(blake2b(b'registar_matricula').hexdigest()+'/', views.registar_matricula, name='registar-matricula'),
    path(blake2b(b'adicioar_disciplina_curso').hexdigest()+'/', views.adicioar_disciplina_curso, name='disciplina-curso'),
    path(blake2b(b'imprimir_ficha_matricula').hexdigest()+'/<int:pk>/', views.imprimir_ficha_matricula, name='imprimir-ficha'),
    path('ajax_cursoID_anoID_retorna_disciplinas/', views.recebe_id_curso_ajax, name='cursoID-anoID-retorna'),
    path(blake2b(b'editar_estudante_matriculado').hexdigest()+'/<int:pk>/', views.editar_estudante_matriculado, name='editar-matricula'),
]
