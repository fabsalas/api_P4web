from django.contrib import admin
from api.models import Cuenta, Libro

# Register your models here.
admin.site.register(Libro)
admin.site.register(Cuenta)