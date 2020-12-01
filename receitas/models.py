from django.db import models
from datetime import datetime
from pessoas.models import Pessoa

# Modelo criado para cadastrar no banco python 
# Com os seguintes comandos realizamos as migrations
# manage.py makemigrations (Cria a pasta migration)
# pessoa é a chave estrangeira
class Receita(models.Model):
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    nome_receita = models.CharField(max_length=200)
    ingredientes = models.TextField()
    modo_preparo = models.TextField()
    tempo_preparo = models.IntegerField()
    rendimento = models.CharField(max_length=100)
    categoria = models.CharField(max_length=100)
    data_receita = models.DateTimeField(default=datetime.now, blank=True)


# python manage.py migrate (Executa as migrations pendentes)