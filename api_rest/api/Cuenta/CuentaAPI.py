from api.Cuenta.CuentaSRL import CuentaSerializer
from api.models import Cuenta
from api.Usuario.UsuarioSRL import UsuarioSerializer
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.views import APIView

class CuentaAPI(APIView):
    def get(self, request, id):
        usuario = User.objects.get(id=id)
        cuenta = Cuenta.objects.get(usuario=usuario)
        
        serializado = CuentaSerializer(cuenta)

        return Response(serializado.data, status=200)