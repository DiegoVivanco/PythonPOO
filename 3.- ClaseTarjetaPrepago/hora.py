# Nombre de la clase
class Hora:
	"""almacena la hora, así como los métodos para manipularla"""

	# Inicializador con sus atributos o propiedades establecidas

	def __init__(self):
		"""Constructor que, por defecto, inicialice las propiedades de la clase a 0 [programación defensiva]."""
		__hora = 0
		__minutos = 0
		__segundos = 0

	def __init__(self, hora = 0, minutos = 0, segundos = 0):
		"""Constructor al que se le pasen como argumentos tres enteros y se los asigna a las propiedades de la clase."""
		self.__hora = hora
		self.__minutos = minutos
		self.__segundos = segundos
		#self.setHora(hora, minutos, segundos)



    # Utilización de setters and getters. Estos métodos especiales sirven para el manejo de las propiedades más importantes del objeto.
    # Métodos set() y get() para todas las propiedades [Abstracción y encapsulamiento].

	def setHora(self, hora, minutos, segundos):
		"""recibe como argumentos tres enteros y se los asigna a las propiedades de la clase. 
		Utiliza el mismo nombre en las variables que reciben los argumentos y en las propiedades de la clase. 
		Este método ha de diseñarse mediante programación por contrato, es decir, debe incluir una precondición"""
		self.__hora = hora if hora >=0 and hora <= 24 else 0
		self.__minutos = minutos if minutos >=0 and minutos <= 60 else 0
		self.__segundos = segundos if segundos >=0 and segundos <= 60 else 0


	def getHora(self):
		"""devuelve la hora como un string de la forma: "horas:minutos:segundos" 
		"""
		return str(self.__hora) + ":" + str(self.__minutos) + ":" + str(self.__segundos)

	def setMinutos(self, minutos):
		self.__minutos = minutos

	def getMinutos(self):
		return self.__minutos

	def setSegundos(self, segundos):
		self.__segundos = segundos

	def getSegundos(self):
		return self.__segundos

    # Comportamientos de la clase Hora

	def imprimirHora(self):
		"""muestra en consola la hora en formato string de la forma: "horas:minutos:segundos"
		"""
		return self.getHora()



if __name__ == '__main__':
	
	hora = Hora()
	hora.setHora(25, -11, -23)
	print (hora.imprimirHora())







#Ejemplo de programación por contrato

#def division(dividendo, divisor):
     #Calculo de la división
     #Pre: Recibe dos números, divisor debe ser distinto de 0.
     #Post: Devuelve un número real, con el cociente de ambos.

    #assert divisor != 0, "El divisor no puede ser 0"
    #return dividendo / ( divisor * 1.0 )

#division(10, 0)
