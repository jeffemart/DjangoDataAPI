from rest_framework import serializers
from .models import MyModel, Chamado

class MyModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyModel
        fields = '__all__'  # Ou especifique os campos que deseja serializar


class ChamadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chamado
        fields = '__all__'