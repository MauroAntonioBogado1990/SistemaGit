from django.contrib import admin
from .models import Localidad, Persona

# puedo poner los modelos de los que voy a colocar
my_models = [Localidad, Persona]

admin.site.register(my_models)
# Register your models here.
