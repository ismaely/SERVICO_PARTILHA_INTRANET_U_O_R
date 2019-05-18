
from helper.includes import *
#from django.views.generic import ListView, DeleteView, DetailView





# Create your views here.
class Home_View(generic.ListView):
    template_name = 'arquivos/home.html'
    def get_queryset(self):
        return None
