#from DNI import *
from Hora import *
class TarjetaPrepago:
	def __init__(self, numeroTelefono = '000000000', nif = '00000000F', saldo = 0):
		self.numeroTelefono = numeroTelefono
		self.saldo = saldo
		#Tiene una Hora
		self.consumo = Hora()
		#tiene un DNI
		#self.dni=DNI(nif)
	def setNumeroTelefono(self, numeroTelefono):
		self.numeroTelefono = numeroTelefono
	def getNumeroTelefono(self):
		return self.numeroTelefono
	def setSaldo(self, saldo):
		self.saldo = saldo
	def getSaldo(self):
		return self.saldo
	def ingresarSaldo(self, ingreso):
		self.setSaldo(self.getSaldo() + ingreso)
	def enviarMensaje(self, numeroMensajes):
		self.setSaldo(self.getSaldo() - 0.09*numeroMensajes)
	def setConsumo(self, hora, minutos, segundos):
		self.consumo.setHora(hora, minutos, segundos)
	def getConsumo(self):
		return self.consumo.getHora()
	def getSegundosConsumo(self):
		segundos = self.consumo.getHoras()*3600 + self.consumo.getMinutos()*60 + self.consumo.getSegundos()
		return segundos
	def realizarLlamada(self, segundos):
		self.setSaldo(self.getSaldo()-0.15-0.01*segundos)
	def consultarTarjeta(self):
			print(self.getSaldo())
			print(self.getNumeroTelefono())
			print(self.getConsumo())
												
				
					
				
				
				
#test

if __name__ == '__main__':
#test set y get
	lebra = TarjetaPrepago()
	test = [[lebra.getConsumo(), '0:0:0' ],
		[lebra.getNumeroTelefono(), '000000000'],
		[lebra.getSaldo(), 0]]
	for miniTest in test:
		if miniTest[0]== miniTest[1]:
			print('ok test de los set y get de las propiedades de la clase')
		else:
			print('fail test de los set y get de las propiedades de la clase')
		lebra.setSaldo(10)
		lebra.setNumeroTelefono(971703716)
		lebra.setConsumo(22,48,52)
		test = [[lebra.getConsumo(), '22:48:52' ],
		[lebra.getNumeroTelefono(), 971703716],
		[lebra.getSaldo(), 10]]
	for miniTest in test:
		if miniTest[0]== miniTest[1]:
			print('ok test de los set y get de las propiedades de la clase')
		else:
			print('fail test de los set y get de las propiedades de la clase')
	#test ingresar saldo
	lebra.ingresarSaldo(10)
	if lebra.getSaldo() == 20:
		print('ok test ingresar saldo')
	else:
		print('fail test ingresar saldo')
	#test enviar mensaje
	lebra.enviarMensaje(100)
	if lebra.getSaldo() == 11:
		print('ok test enviar mensaje')
	else:
		print('fail test enviar mensaje')
	#test consumo en segundos
	lebra.setConsumo(22,48,52)
	if lebra.getSegundosConsumo() == 82132:
			print('ok test consumo en segundos')
	else:
			print('fail test consumo en segundos')
	#test realizar llamada
	lebra.setSaldo(100)
	lebra.realizarLlamada(85)
	if lebra.getSaldo() == 99:
		print('OK test realizar llamada')
	else:
		      print('fail test realizar llamada')
	#test consultarTarjeta
	lebra.consultarTarjeta()
			
	
	
		
		
		
	
	
	
		
		
		
