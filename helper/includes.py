#ficheiro onde vai constar todos include que seram usado

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from helper.opcoes_escolha import GENERO, PROVINCIA
