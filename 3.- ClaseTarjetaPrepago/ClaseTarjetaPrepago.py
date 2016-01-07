from dni import *
from hora import *

# Nombre de la clase

class TarjetaPrepago:
	"""permite interactuar con la información almacenada en una tarjeta de telefonía móvil prepago"""

	# Inicializador con sus atributos o propiedades establecidas

	def __init__(self):
		"""Constructor que inicializa las propiedades de la clase (programación defensiva)."""
		__numeroTelefono = ""
		__nif = Dni()
		__saldo = float
		__consumo = Hora()

	def __init__(self, numeroTelefono = "", nif = "", saldo = 0.0, consumo = ""):
		"""Constructor que recibe como argumentos los valores para las propiedades de clase numeroTelefono , NIF y saldo"""
		self.__numeroTelefono = numeroTelefono
		self.__nif = Dni(cadena = nif)
		self.__saldo = saldo
		self.__consumo = Hora()

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

	def setConsumo(self,consumo):
		self.__consumo = consumo

	def getConsumo(self):
		return self.__consumo



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
		#print ("Tiempo de consumo: ", self.getConsumo())


	def convierteASegundos(self):
		"""convertir la hora (hora:minutos:segundos) a segundos para poder sumar la duración de la llamada al total de la duración
        de las llamadas en la propiedad consumo"""
		minutos = self.horas * 60 + self.minutos
		segundos = self.minutos * 60 + self.segundos
		return segundos




if __name__ == '__main__':
	tarjetaPrepago = TarjetaPrepago()
	tarjetaPrepago.setNumeroTelefono("564564654")
	tarjetaPrepago.setNif("45610975C")
	tarjetaPrepago.setSaldo(100)
	tarjetaPrepago.consultarTarjeta()

	print ("\n")

	cantidadIngresada, dineroActualizado = tarjetaPrepago.ingresarSaldo(100)
	consumido, cantidadMensajes, saldoRestante = tarjetaPrepago.enviarMensaje(10)
	segundosHablados, dineroConsumido, dineroRestante = tarjetaPrepago.realizarLlamada(200)

	print ("Se ha ingresado:",str(cantidadIngresada),"euros del saldo disponible, tu saldo actual es de:", str(dineroActualizado), "euros")
	print ("Por la cantidad de:",str(cantidadMensajes),"Mensajes, se ha descontado:",str(consumido), " euros del saldo disponible, tu saldo actual es de:", str(saldoRestante), "euros")
	print ("La duracion de la llamada es:",str(segundosHablados),"segundos, se ha descontado:",str(dineroConsumido), "euros del saldo disponible, tu saldo actual es de:", str(dineroRestante), "euros")

