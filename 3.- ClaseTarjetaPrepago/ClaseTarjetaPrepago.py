from dni import *
from hora import *

# Nombre de la clase

class TarjetaPrepago:
	"""permite interactuar con la información almacenada en una tarjeta de telefonía móvil prepago"""

	# Inicializador con sus atributos o propiedades establecidas
	def __init__(self, numeroTelefono = "", nif = "", saldo = 0.0, consumo = ""):
		"""Constructor que recibe como argumentos los valores para las propiedades de clase numeroTelefono , NIF y saldo"""
		self.__numeroTelefono = numeroTelefono
		self.__nif = Dni(cadena = nif)
		self.__saldo = saldo
		self.consumo = Hora()

    # Utilización de setters and getters. Estos métodos especiales sirven para el manejo de las propiedades más importantes del objeto
    # Métodos set() y get() para todas las propiedades [Abstracción y encapsulamiento].

	def setNumeroTelefono(self, numeroTelefono):
		self.__numeroTelefono = numeroTelefono

	def getNumeroTelefono(self):
		return self.__numeroTelefono

	def setNif(self, nif):
		self.__nif = nif

	def getNif(self):
		return self.__nif

	def setSaldo(self, saldo):
		self.__saldo = saldo

	def getSaldo(self):
		return self.__saldo

	def setConsumo(self, hora, minutos, segundos):
		self.consumo.setHora(hora, minutos, segundos)

	def getConsumo(self):
		return self.consumo.getHora()

	def getSegundosConsumo(self):
		segundos = self.consumo.getHoras()*3600 + self.consumo.getMinutos()*60 + self.consumo.getSegundos()
		return segundos




# Comportamientos de la clase TarjetaPrepago

	def ingresarSaldo(self, cantidadIngresada):
		"""añade al saldo una cantidad de dinero"""

		#dineroTotal = self.getSaldo() + cantidadIngresada
		#############################################################

		dineroActualizado = self.getSaldo() + cantidadIngresada
		self.setSaldo(dineroActualizado)
		return (cantidadIngresada, dineroActualizado)
		#############################################################

		#return self.getSaldo() + cantidadIngresada

	def enviarMensaje(self, cantidadMensajes, precioMensaje = 0.09):
		"""recibe como argumento un entero que representa un número de mensajes a enviar, y resta al saldo 9 centimos por mensaje"""		
		#if self.getSaldo() >= 0:
		#	return self.getSaldo() - (cantidadMensajes * precioMensaje)
		#else:
		#	print ("Tu saldo no te permite realizar el mensaje")
		##############################################################

		if self.getSaldo() >= 0:
			consumido = cantidadMensajes * precioMensaje
			saldoRestante = self.getSaldo() - consumido
			self.setSaldo(saldoRestante)
			return (consumido, cantidadMensajes, saldoRestante)
		else:
			print ("Tu saldo no te permite realizar el mensaje")

	def realizarLlamada(self, segundosHablados, establecimientoLLamada = 0.15, tarifaLlamada = 0.01):
		"""recibe un entero que representa el número de segundos hablados. Se restará al saldo la cantidad correspondiente calculada en base a 15 céntimos por
		establecimiento de llamada y 1 céntimo por segundo. También se actualizará la propiedad consumo"""

		#return self.getSaldo() - ((segundosHablados * tarifaLlamada) + establecimientoLLamada)
		###############################################################################################

		#gastado = self.getSaldo() - ((segundosHablados * tarifaLlamada) + establecimientoLLamada)
		#resto = self.__saldo - gastado
		#self.setSaldo(resto)
		#return gastado
		###############################################################################################

		dineroConsumido = ((segundosHablados * tarifaLlamada) + establecimientoLLamada)
		dineroRestante = self.getSaldo() - dineroConsumido
		self.setSaldo(dineroRestante)
		return (segundosHablados, dineroConsumido, dineroRestante)

	def consultarTarjeta(self):
		"""visualizará todos los datos de la tarjeta en consola."""
		print ("Numero de telefono:", self.getNumeroTelefono())
		print ("Con DNI:", self.getNif())
		print ("Saldo disponible:", self.getSaldo(), "euros")
		print ("Tiempo de consumo: ", self.getConsumo())







if __name__ == '__main__':

	claro = TarjetaPrepago()

	print ("Casos Test sobre los set y get de las propiedades de la clase")
	test = [[claro.getConsumo(), '0:0:0' ],
		[claro.getNumeroTelefono(), ""],
		[claro.getSaldo(), 0]]
	
	for miniTest in test:
		if miniTest[0]== miniTest[1]:
			print('ok test de los set y get de las propiedades de la clase')
		else:
			print('fail test de los set y get de las propiedades de la clase')
	
	print ("Casos Test sobre los set y get de las propiedades de la clase")
	claro.setSaldo(10)
	claro.setNumeroTelefono(971703716)
	claro.setNif(7788777)
	claro.setConsumo(22,48,52)
	test = [[claro.getConsumo(), '22:48:52' ],
	[claro.getNumeroTelefono(), 971703716],
	[claro.getSaldo(), 10]]
	
	for miniTest in test:
		if miniTest[0]== miniTest[1]:
			print('ok test de los set y get de las propiedades de la clase')
		else:
			print('fail test de los set y get de las propiedades de la clase')

###########################################################################################


#test ingresar saldo
	print ("\n")

	claro.ingresarSaldo(10)
	if claro.getSaldo() == 20:
		print('ok test ingresar saldo')
	else:
		print('fail test ingresar saldo')

###########################################################################################

#test enviar mensaje

	claro.enviarMensaje(100)
	if claro.getSaldo() == 11:
		print('ok test enviar mensaje')
	else:
		print('fail test enviar mensaje')

###########################################################################################

#test consumo en segundos

	claro.setConsumo(22,48,52)
	if claro.getSegundosConsumo() == 82132:
			print('ok test consumo en segundos')
	else:
			print('fail test consumo en segundos')

###########################################################################################

#test realizar llamada


	claro.setSaldo(100)
	claro.realizarLlamada(85)
	if claro.getSaldo() == 99:
		print('OK test realizar llamada')
	else:
		      print('fail test realizar llamada')
	
###########################################################################################

#test consultarTarjeta
	print ("\nCaso Test consultarTarjeta\n")
	claro.consultarTarjeta()


###########################################################################################

# Ejemplo manejo de la Clase TarjetaPrepago
	print ("\nEjemplo manejo de la Clase TarjetaPrepago\n")
	tarjetaPrepago = TarjetaPrepago()
	tarjetaPrepago.setNumeroTelefono("564564654")
	tarjetaPrepago.setNif("45610975C")
	tarjetaPrepago.setSaldo(100)
	tarjetaPrepago.setConsumo(2,4,52)
	tarjetaPrepago.consultarTarjeta()

	print ("\n")

	cantidadIngresada, dineroActualizado = tarjetaPrepago.ingresarSaldo(100)
	consumido, cantidadMensajes, saldoRestante = tarjetaPrepago.enviarMensaje(10)
	segundosHablados, dineroConsumido, dineroRestante = tarjetaPrepago.realizarLlamada(200)

	print ("Se ha ingresado:",str(cantidadIngresada),"euros del saldo disponible, tu saldo actual es de:", str(dineroActualizado), "euros")
	print ("Por la cantidad de:",str(cantidadMensajes),"Mensajes, se ha descontado:",str(consumido), " euros del saldo disponible, tu saldo actual es de:", str(saldoRestante), "euros")
	print ("La duracion de la llamada es:",str(segundosHablados),"segundos, se ha descontado:",str(dineroConsumido), "euros del saldo disponible, tu saldo actual es de:", str(dineroRestante), "euros")













	#def convierteASegundos(self):
	#	"""convertir la hora (hora:minutos:segundos) a segundos para poder sumar la duración de la llamada al total de la duración
    #    de las llamadas en la propiedad consumo"""
	#	minutos = self.horas * 60 + self.minutos
	#	segundos = self.minutos * 60 + self.segundos
	#	return segundos