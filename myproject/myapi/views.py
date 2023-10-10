from rest_framework import viewsets
from .models import Chamado
from .serializers import ChamadoSerializer


class ChamadoViewSet(viewsets.ModelViewSet):
    queryset = Chamado.objects.all()
    serializer_class = ChamadoSerializer