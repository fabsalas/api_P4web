from rest_framework.response import Response
from rest_framework.views import APIView

from api.models import Libro
from api.Libro.libroSRL import LibroSerializer
from rest_framework.permissions import IsAuthenticated

class LibroAPI(APIView):
    permission_classes = [IsAuthenticated] #para verificar que existe una autentificación.
    
    def get(self, request, id):
        try: 
            libros= Libro.objects.all()
            serializer = LibroSerializer(libros, many = True) #many = True para que me genere una lista

            return Response(serializer.data, status=200)
        except:
                return Response(status=400)

    def post(self, request):
        #data = request.data
        serializer= LibroSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        else:
            return Response(serializer.errors, status=400)

        

    def put(self, request, id):
        data = request.data
        libro = Libro.objects.get(id=id)
        serializer = LibroSerializer(libro, data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(status=200)
        else:
            return Response(serializer.errors, status=400)

    def delete(self, request, id):
        libro = Libro.objects.get(id=id)
        libro.delete()

        return Response(status=200)