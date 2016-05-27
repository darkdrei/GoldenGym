from django.contrib import admin
from .models import Persona,Ejercicio,Rutina,Producto,Menudeo,Compra,TipoPago,Pago,Musculo,Entrenamiento,EjercicioDeEntrenamiento,Rutina,EntrenamientoDeRutina

# Register your models here.
admin.site.register(Persona)
admin.site.register(Ejercicio)
admin.site.register(Rutina)
admin.site.register(Producto)
admin.site.register(Menudeo)
admin.site.register(Compra)
admin.site.register(TipoPago)
admin.site.register(Pago)
admin.site.register(Musculo)
admin.site.register(Entrenamiento)
admin.site.register(EjercicioDeEntrenamiento)
admin.site.register(EntrenamientoDeRutina)
