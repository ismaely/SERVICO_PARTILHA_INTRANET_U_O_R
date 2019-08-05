from django.urls import path
from . import views



app_name = 'biblioteca'
urlpatterns = [
    path('cadastrar_livro/', views.cadastrar_livro, name='cadastrar-livro'),
    path('listar_livros/', views.listar_livros, name='listar-livro'),

]
