from django.db import models

class MyModel(models.Model):
    # Defina os campos do seu modelo aqui
    field1 = models.CharField(max_length=100)
    field2 = models.IntegerField()
    # ...

    def __str__(self):
        return self.field1  # Isso é apenas um exemplo; você pode escolher como deseja representar seu modelo
    
class Chamado(models.Model):
    CodInterno = models.IntegerField()
    CodChamado = models.CharField(max_length=10)
    DataCriacao = models.DateTimeField()
    DataFinalizacao = models.DateTimeField()
    SequenciaCategoria = models.CharField(max_length=50)
    HoraFinalizacao = models.CharField(max_length=10)
    TotalHorasAberturaFinalizacao = models.FloatField()
    FirstCall = models.CharField(max_length=3)
    ChaveOperador = models.IntegerField()
    ChaveUsuario = models.IntegerField()
    ChaveSla = models.IntegerField(null=True, blank=True)