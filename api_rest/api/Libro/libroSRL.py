

from api.models import Libro
from rest_framework import serializers

class LibroSerializer(serializers.ModelSerializer):
    id= serializers.IntegerField(required=False)
    nombre = serializers.CharField(required=False)
    class Meta:
        model =Libro
        fields ='__all__' #trae todos los elementos
