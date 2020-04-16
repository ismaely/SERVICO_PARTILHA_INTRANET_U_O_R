from django.db import models
from secretaria.models import Pessoa
from django.contrib.auth.models import User

# Create your models here.


class Utilizador_User(models.Model):
    pessoa= models.ForeignKey(Pessoa, on_delete=models.CASCADE, parent_link=True)
    user= models.ForeignKey(User, on_delete=models.CASCADE, parent_link=True)

    def __str__ (self):
        return '%d' % (self.id)
