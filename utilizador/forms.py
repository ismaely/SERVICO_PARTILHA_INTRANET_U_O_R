from secretaria.models import Pessoa
from utilizador.models import Utilizador_User
from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm
from helper.opcoes_escolha import CATEGORIA_UTILIZADOR
import helper.core



class LoginForm(forms.Form):
    senha = forms.CharField(max_length=20, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    nome_utilizador = forms.CharField(max_length=80, widget=forms.TextInput(attrs={'class': 'form-control'}))



class Utilizador_Form(forms.Form):
    bi = forms.CharField(max_length=14, widget=forms.TextInput(attrs={'class': 'form-control maiuscula'}))
    #senha = forms.CharField(max_length=50, required=False, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    nome_utilizador = forms.CharField(max_length=80, required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'sofia.filipe'}))
    categoria = forms.CharField(max_length=50, widget=forms.Select(choices=CATEGORIA_UTILIZADOR, attrs={'class': 'form-control'}))

    def clean_bi(self):
        value = self.cleaned_data.get('bi')
        bi = helper.core.retorna_id_simples(value)
        if bi ==  0:
            raise forms.ValidationError("O Número do B.I não é valido")
        return bi


    def clean_nome_utilizador(self):
        nome_utilizador =str(self.cleaned_data.get('nome_utilizador'))
        try:
            if nome_utilizador.count('.') == 1:
                resp = len(nome_utilizador) - nome_utilizador.find('.')
                if nome_utilizador.find('.') != 2 and resp > 2:

                    nome = User.objects.get(username=nome_utilizador)
                    if nome.username == nome_utilizador:
                        raise forms.ValidationError("O nome já existe...!")
                    else:
                        return nome_utilizador
                else:
                    raise forms.ValidationError("O ponto(.) não é valido nesta posição!")
            else:
                raise forms.ValidationError("O nome de utilizador não é valido, só deve ter um ponto(.)! Exemplo: sofia.filipe")
        except User.DoesNotExist:
            return nome_utilizador
