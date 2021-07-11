from django.db import models

# Create your models here.
class Edificio(models.Model):
	# Opciones para el atributo 'tipo'
	opciones_tipo = (
	    ('residencial','Residencial'),
	    ('comercial','Comercial'),
    )
    
	nombre = models.CharField("Nombre del edificio", max_length=50)
	direccion = models.CharField("Dirección", max_length=50)
	ciudad = models.CharField("Ciudad", max_length=50)
	tipo_edificio = models.CharField("Tipo", max_length=30, 
        choices=opciones_tipo) 

	def __str__(self):
	    return "%s %s %s %s" % (
            self.nombre,
            self.direccion,
            self.ciudad,
            self.tipo_edificio
        )

# Método para obtener la información referente al edificio:
    #   Número total de cuartos
	def obtener_cantidad_cuartos(self):
		valor = [t.numero_cuar for t in self.departamentos.all()]
		valor = sum(valor)

		return valor

    # Costo total de los departamentos
	def obtener_costo_departamento(self):
		valor = [t.costo_depar for t in self.departamentos.all()]
		valor = sum(valor) 

		return valor

class Departamento(models.Model):
	nombre_pro = models.CharField("Propietario/a", max_length=100) #Nombre del propietario
	costo_depar = models.DecimalField("Costo",max_digits=100, decimal_places=2) #Costo departamento
	numero_cuar = models.IntegerField("Número de cuartos") #Numero de cuartos
	edificio = models.ForeignKey(Edificio, on_delete=models.CASCADE,
	        related_name="departamentos")

	def __str__(self):
		return "%s %.2f %d %s" % (
            self.nombre_pro, 
			self.costo_depar,
			self.numero_cuar,
			self.edificio
        )

