from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=150)
    email = models.EmailField()
    endereco = models.CharField(max_length=350)

    def __str__(self):
        return self.nome

class Categoria(models.Model):
    nome = models.CharField(max_length=250)

    def __str__(self):
        return self.nome

class Filme(models.Model):
    titulo = models.CharField(max_length=250)
    ano_lancamento = models.IntegerField()
    valor_locacao = models.FloatField()
    Categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo


class Locacao(models.Model):
    data_entrega = models.DateField()
    data_locacao = models.DateField()
    valor = models.IntegerField()
    Cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    Filme = models.ManyToManyField(Filme)