from rest_framework.response import Response
from rest_framework.views import APIView

from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from rest_framework.authtoken.models import Token


class LoginAPI(APIView):
    def post(self, request):
        data = request.databases

        username = data['username']
        password = data['password']

        try:
            user = User.objects.get(username=username)
        except:
            return Response({"Error": "Usuario no es valido"}, status=400)

        password_valido = check_password(password, user.password)

        if(password_valido):
            token, created = Token.objects.get_or_create(user=user)
            return Response({"Token": token.key}, status=200)
        else:
            return Response({"Error": "Contraseña no es valida."}, status=400)

#api que elimina el token 
class LogoutAPI(APIView):
    def post(self, request):
        try:
            data = request.data
            token = data['token']
            token= Token.objects.filter(key = token)
            token.delete()

            return Response({"Token Eliminado correctamente"}, status=200)
        except:
            return Response({"Error": "token no ha sido eliminado"}, status=400)
