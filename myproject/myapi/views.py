from rest_framework import viewsets
from .models import Chamado
from .serializers import ChamadoSerializer
from drf_yasg.utils import swagger_auto_schema


class ChamadoViewSet(viewsets.ModelViewSet):
    queryset = Chamado.objects.all()
    serializer_class = ChamadoSerializer

    # exemplo de metodo para esconder algum REST que não queira
    # @swagger_auto_schema(auto_schema=None)
    # def partial_update(self, request, *args, **kwargs):
    #     return super().partial_update(request, *args, **kwargs)