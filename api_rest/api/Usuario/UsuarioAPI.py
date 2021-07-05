from api.Usuario.UsuarioAPI import UsuarioSerializer
from django.contrib.auth.models import User
from  rest_framework.response import response
from rest_framework.views import APIView

class UsuarioAPI(APIView):
    def get(self, request):
        usuarios= User.objects.all()
        serializers= UsuarioSerializer(usuarios, many=True)
        print(serializers.data)
        
        return response(serializers.data, status=200)