

from api.models import Libro
from rest_framework import serializers

class LibroSerializer(serializers.ModelSerializer):
    id          = serializers.IntegerField(required=False)
    nombre      = serializers.CharField(required=False)
    autor       = serializers.CharField (required = False )
    sinopsis    = serializers.CharField (required = False )
    precio      = serializers.IntegerField(required = False )
    stock       = serializers.IntegerField(required = False )
    publicacion = serializers.DateField(required = False ) 
    class Meta:
        model = Libro
        fields ='__all__' #trae todos los elementos
