from django.contrib.auth.models import User
from rest_framework import serializers

class UsuarioSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=False)
    email = serializers.EmailField(required=False)
    firstname = serializers.CharField(required=False)

    class Meta:
        model = User
        fields =['username', 'email','firstname']