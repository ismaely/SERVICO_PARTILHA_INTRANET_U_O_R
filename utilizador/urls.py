from django.urls import path
from . import views


app_name = 'utilizador'
urlpatterns = [
    path('', views.login_utilizador, name='login_utilizador'),
    path('login/', views.login_utilizador, name='login-home'),
    path('accounts/login/', views.login_utilizador, name='login'),
    path('sair/', views.sair, name='sair'),
    path('criar_conta_utilizador/', views.criar_conta_utilizador, name='criar-utilizador'),
    path('listar_utilizador/', views.listar_utilizador, name='listar'),
    path('eliminar_conta/<int:pk>/', views.eliminar_conta, name='eliminar_conta'),
    path('desativar_conta/<int:pk>/', views.desativar_conta, name='desativar'),
    path('ativar_conta/<int:pk>/', views.ativar_conta, name='ativar'),
]
