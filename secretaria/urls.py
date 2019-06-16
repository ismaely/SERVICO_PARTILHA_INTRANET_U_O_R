from django.urls import path
from . import views

app_name = 'secretaria'
urlpatterns = [
    path('', views.Home_View.as_view(), name='home'),
    path('home/', views.Home_View.as_view(), name='home-kanguitu'),
    path('login/', views.login, name='login'),
    path('registar_cadastro/', views.Registar_cadastro, name='registar-cadastro'),
    path('municipio_retorna', views.retorna_municipio, name='municipio-retorna'),
    path('registar_orientador_tese/', views.registar_professor_orientarTese, name='orientador-tese'),
    path('registar_tema_monografia/', views.registar_tema_monografia, name='registar-tema-monografia'),
    path('registar_solicitacao_tema_monografia/', views.registar_solicitacao_tema_monografia, name='registar-solicitacao-monografia'),
    path('registar_reclamacao/', views.registar_reclamacao, name='registar-reclamacao'),
    path('registar_trabalho_fim_curso/', views.registar_trabalho_fim_curso, name='registar-trabalho-fim_curso'),
    path('registar_defesa_final_curso_aluno/', views.registar_defesa_final_curso_aluno, name='registar-defesa-final'),
    path('registar_nota_aluno/', views.registar_nota_aluno, name='registar-nota-aluno'),
    path('registar_curso/', views.registar_cursos, name='registar-cursos'),
    path('registar_disciplina/', views.registar_disciplina, name='registar-disciplina'),


]
