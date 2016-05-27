from django.db import models

# Create your models here.

class Persona(models.Model):	
	nombre = models.CharField(max_length=30)
	primerApellido = models.CharField(max_length=30)
	segundoApellido = models.CharField(max_length=30)
	fechaNacimiento = models.DateField()
	fechaIngreso = models.DateField()
	email = models.EmailField()
	direccion = models.CharField(max_length=30)

	def __unicode__(self):
		return self.nombre

class Cliente(Persona):

	def __unicode__(self):
		return self.nombre
	#end def

#end class

	


class Ejercicio(models.Model):
	nombre = models.CharField(max_length=30)
	descripcion = models.TextField(max_length=30)
	estado = models.BooleanField()

	def __unicode__(self):
		return self.nombre
	#end def
#end class

class Rutina(models.Model):
	nombre = models.CharField(max_length=30)
	estado = models.BooleanField()

	def __unicode__(self):
		return self.nombre
	#end def

#end class


class Producto(models.Model):
	nombre = models.CharField(max_length=30)
	precio = models.FloatField()
	cantidad = models.IntegerField()
	existencias = models.IntegerField()
	estado = models.BooleanField()

	def __unicode__(self):
		return self.nombre
	#end def

#end class

class Menudeo(models.Model):
	precio = models.FloatField()
	estado = models.BooleanField()
	producto = models.ForeignKey(Producto)


	def __unicode__(self):
		return self.producto.nombre
	#end def

#end class

class Compra(models.Model):
	precio = models.FloatField()
	cantidad = models.IntegerField()
	estado = models.BooleanField()
	menudeo = models.ForeignKey(Menudeo)

class TipoPago(models.Model):
	nombre = models.CharField(max_length=30)
	valor = models.FloatField()
	estado = models.BooleanField()
	descripcion = models.TextField(max_length=30)

class Pago(models.Model):
	estado = models.BooleanField()
	valor = models.FloatField()
	fecha_realizacion = models.DateField()
	fecha_fin = models.DateField()
	cliente = models.ForeignKey(Cliente)
	tipoPago = models.ForeignKey(TipoPago)

class Musculo(models.Model):
	nombre = models.CharField(max_length=30)
	estado = models.BooleanField()

class Entrenamiento(models.Model):
	nombre = models.CharField(max_length=30)
	estado = models.BooleanField()
	musculo = models.ForeignKey(Musculo)

class EjercicioDeEntrenamiento(models.Model):
	serie = models.IntegerField()
	repeticiones = models.IntegerField()
	estado = models.BooleanField()
	entrenamiento = models.ForeignKey(Entrenamiento)
	ejercicio = models.ForeignKey(Ejercicio)

class Rutina(models.Model):
	nombre = models.CharField(max_length=30)
	estado = models.BooleanField()

class EntrenamientoDeRutina(models.Model):
	entrenamiento = models.ForeignKey(Entrenamiento)
	rutina = models.ForeignKey(Rutina)

