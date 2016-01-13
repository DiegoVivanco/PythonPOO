# Nombre de la clase
class Hora:
	"""almacena la hora, así como los métodos para manipularla"""

	# Inicializador con sus atributos o propiedades establecidas


	def __init__(self, hora = 0, minutos = 0, segundos = 0):
		"""Constructor al que se le pasen como argumentos tres enteros y se los asigna a las propiedades de la clase."""
		self.__hora = hora
		self.__minutos = minutos
		self.__segundos = segundos
		#self.setHora(hora, minutos, segundos)



    # Utilización de setters and getters. Estos métodos especiales sirven para el manejo de las propiedades más importantes del objeto.
    # Métodos set() y get() para todas las propiedades [Abstracción y encapsulamiento].

	def setHoras(self, hora):
		self.__hora = hora if hora >=0 and hora < 24 else 0

	def getHoras(self):
		return self.__hora

	def setMinutos(self, minutos):
		self.__minutos = minutos if minutos >=0 and minutos <= 60 else 0

	def getMinutos(self):
		return self.__minutos

	def setSegundos(self, segundos):
		self.__segundos = segundos if segundos >=0 and segundos <= 60 else 0

	def getSegundos(self):
		return self.__segundos

	# Comportamientos de la clase Hora
	def setHora(self, hora, minutos, segundos):
		"""recibe como argumentos tres enteros y se los asigna a las propiedades de la clase. 
		Utiliza el mismo nombre en las variables que reciben los argumentos y en las propiedades de la clase. 
		Este método ha de diseñarse mediante programación por contrato, es decir, debe incluir una precondición"""
		self.__hora = hora if hora >=0 and hora < 24 else 0
		self.__minutos = minutos if minutos >=0 and minutos <= 60 else 0
		self.__segundos = segundos if segundos >=0 and segundos <= 60 else 0


	def getHora(self):
		"""devuelve la hora como un string de la forma: "horas:minutos:segundos" 
		"""
		return '%s:%s:%s' %(self.__hora,self.__minutos,self.__segundos)
	def imprimirHora(self):
		"""muestra en consola la hora en formato string de la forma: "horas:minutos:segundos"
		"""
		print (self.getHora())



if __name__ == '__main__':

#Casos Test sobre los set y get de las propiedades de la clase

	ecuador = Hora()
	test = [[ecuador.getHoras(), 0 ],
		[ecuador.getMinutos(), 0],
		[ecuador.getSegundos(), 0],
		[ecuador.getHora(),'0:0:0']]

	print ("Casos Test sobre los set y get de las propiedades de la clase")
	for miniTest in test:
		if miniTest[0]== miniTest[1]:
			print('ok test de los set y get de las propiedades de la clase')
		else:
			print('fail test de los set y get de las propiedes de la clase')

		
	ecuador.setHoras(1)
	ecuador.setMinutos(1)
	ecuador.setSegundos(1)
	test = [[ecuador.getHoras(), 1 ],
		[ecuador.getMinutos(), 1 ],
		[ecuador.getSegundos(), 1 ]]

	print ("Casos Test sobre los set y get de las propiedades de la clase")
	for miniTest in test:
		if miniTest[0]== miniTest[1]:
			print('ok test de los set y get de las propiedades de la clase')
		else:
			print('fail test de los set y get de las propiedades de la clase')

	print ("Casos Test sobre los set y get de las propiedades de la clase")		
	ecuador.setHora(2,2,2)
	if ecuador.getHora()== '2:2:2':
		print('ok test de los set y get de las propiedades de la clase')
	else:
		print('fail test de los set y get de las propiedades de la clase')

###########################################################################################

#test check
	ecuador.setHoras(100)
	ecuador.setMinutos(100)
	ecuador.setSegundos(100)
	test = [[ecuador.getHoras(), 0 ],
		[ecuador.getMinutos(), 0],
		[ecuador.getSegundos(), 0],
		[ecuador.getHora(),'0:0:0']]
	for miniTest in test:
		if miniTest[0]== miniTest[1]:
			print('ok test check')
		else:
			print('fail test check')
	


#Ejemplo manejo de la CLase Hora, (24:11:23 se tiene que representar como 0:11:23)
	hora = Hora()
	hora.setHora(22, 48, 52)
	hora.imprimirHora()
	print (hora.getHoras())


#Ejemplo de programación por contrato

#def division(dividendo, divisor):
     #Calculo de la división
     #Pre: Recibe dos números, divisor debe ser distinto de 0.
     #Post: Devuelve un número real, con el cociente de ambos.

    #assert divisor != 0, "El divisor no puede ser 0"
    #return dividendo / ( divisor * 1.0 )

#division(10, 0)
