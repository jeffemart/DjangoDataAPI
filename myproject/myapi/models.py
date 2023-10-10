from django.db import models

    
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