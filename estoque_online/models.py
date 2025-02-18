from django.db import models

class cadastrar_produtos(models.Model):
    nome_do_produto = models.CharField(max_length=100)
    codigo_de_barra = models.BigIntegerField()
    quantidade_total = models.IntegerField()
    localizacao = models.IntegerField()
    
    def __str__(self):
        return self.nome_do_produto
