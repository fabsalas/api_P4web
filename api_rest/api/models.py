from django.db import models

# Create your models here.

Class Libro(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=99)
    autor = models.CharField(max_length=99)
    sinopsis = models.TextField
    precio= models.IntegerField(default=0)
    stock= models.IntegerField(default=0)
    publicacion = models.DateField
