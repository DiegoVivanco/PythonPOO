# Nombre de la clase
class Fecha:
	"""representa el tipo de dato fecha como tres enteros de nombres:  dia , mes y año"""
    
    # Inicializador con sus atributos o propiedades establecidas

	def __init__(self):
		"""Constructor que, por defecto, inicializa las propiedades de la clase a la fecha 01-01-1900 [programación defensiva]."""
		dia = 1
		mes = 1
		anyo = 1900

	def __init__(self, dia = 1, mes = 1, anyo = 1900):
		"""Constructor al que se le pasen como argumentos tres enteros y se los asigne a las propiedades de la clase."""
		self.dia = dia
		self.mes = mes
		self.anyo = anyo

    
    # Utilización de setters and getters. Estos métodos especiales sirven para el manejo de las propiedades más importantes del objeto.
    # Métodos set() y get() para todas las propiedades [Abstracción y encapsulamiento].

	def setFecha(self, dia, mes, anyo):
		"""setFecha() que recibe como argumentos tres enteros y se los asigna a las propiedades de la clase
		(utiliza el mismo nombre en las variables que reciben los argumentos y en las propiedades de la clase). Este método ha
		de diseñarse mediante programación por contrato, es decir, debe incluir una precondición"""
		self.dia = dia if dia >= 1 and dia <= 31 else 1
		self.mes = mes if mes >= 1 and mes <= 12 else 1
		self.anyo = anyo if anyo >= 1900 and anyo <= 300 else 1900

	def getFecha(self):
		return str(self.getDia()) + "-" + str(self.getMes()) + "-" + str(self.getAnyo())

	def setDia(self, dia):
		self.dia = dia

	def getDia(self):
		return self.dia

	def setMes(self, mes):
		self.mes = mes

	def getMes(self):
		return self.mes

	def setAnyo(self, anyo):
		self.anyo = anyo

	def getAnyo(self):
		return self.anyo


    # Comportamientos de la clase Hora

	def incrementarFecha(self, numeroDias):
		"""recibe un entero que representa un número de días e incrementa la fecha en dicha cantidad de dias"""
		return self.getDia() + numeroDias

	def __mesLetra(self):
		"""devuelve el mes en letras asociado al mes numérico guardado en una determinada instancia (objeto) de la clase"""

		mesesAnyo = ['enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio', 'julio', 'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre']
		return mesesAnyo[self.getMes() -1]


	def imprimirFecha(self):
		"""escribe la fecha en el formato dia-mes-año en consola. Se mostrará el nombre del mes, no el número."""
		print (self.getDia(),"-",self.__mesLetra(),"-",self.getAnyo())



if __name__ == '__main__':
	
	fecha = Fecha()
	fecha.setFecha(0,0,0)
	print (fecha.getFecha())
	fecha.imprimirFecha()
	print (fecha.incrementarFecha(10))