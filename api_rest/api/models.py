from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Libro(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=99)
    autor = models.CharField(max_length=99)
    sinopsis = models.TextField(null=True)
    precio= models.IntegerField(default=0)
    stock= models.IntegerField(default=0)
    publicacion = models.DateField(null=True)

class Cuenta(models.Model):
    usuario= models.OneToOneField(User, on_delete=models.CASCADE)
    libros= models.ManyToManyField(Libro)