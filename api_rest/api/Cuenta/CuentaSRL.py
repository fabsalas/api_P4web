
from api.Usuario.UsuarioSRL import UsuarioSerializer
from api.models import Cuenta
from rest_framework import serializers

class CuentaSerializer(serializers.ModelSerializer):
    usuario = UsuarioSerializer(required = False)
    

    class Meta:
        model = Cuenta
        fields = ['usuario']