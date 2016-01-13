#habria que importar la clase dni para completar correctamente el ejercicio
from dni import *
class CuentaCorriente:
	def __init__(self, nombre = "Mr.Nobody", apellidos = "noone", direccion = "nowhere", telefono = "000000000", saldo = 0):
		self.nombre = nombre
		self.apellidos = apellidos
		self. direccion = direccion	
		self.telefono = telefono
		self.saldo = saldo
#		self.dni = DNI()
	def getNombre(self):
		return self.nombre
	def setNombre(self, nombre):
		self.nombre = nombre
	def getApellidos(self):
		return self.apellidos 
	def setApellidos(self, apellidos):
		self.apellidos = apellidos
	def getDireccion(self):
		return self.direccion 
	def setDireccion(self, direccion):
		self.direccion = direccion
	def getTelefono(self):
		return self.telefono
	def setTelefono(self, telefono):
		self.telefono = telefono
	def getSaldo(self):
		return self.saldo
	def setSaldo(self, saldo):
		self.saldo = saldo
	def retirarDinero(self, dinero):
		self.setSaldo( self.getSaldo() - dinero)
	def ingresarDinero(self, dinero):
		self.setSaldo( self.getSaldo() + dinero)
	def consultarCuenta(self):
		print(self.getNombre() ,self.getApellidos(), self.getDireccion(), self.getTelefono(), self.getSaldo())
	def saldoNegativo(self):
		if self.getSaldo() < 0:
			return True
		else:
			return False



#test
#test de los set y get de las propiedades de la clase
if __name__ == '__main__':
	miCuenta = CuentaCorriente()
	test=[[miCuenta.getNombre(),"Mr.Nobody"],
	[miCuenta.getApellidos(), "noone"],
	[miCuenta.getDireccion(), "nowhere"],
	[miCuenta.getTelefono(), "000000000"],
	[miCuenta.getSaldo(), 0]]
	for miniTest in test:
		if miniTest[0]== miniTest[1]:
			print('ok test de los set y get de las propiedades de la clase')
		else:
			print('fail test de los set y get de las propiedades de la clase')


	miCuenta.setNombre('Ricardo')
	miCuenta.setApellidos('Garrido')
	miCuenta.setDireccion('Palma')
	miCuenta.setTelefono('617382654')
	miCuenta.setSaldo(120)
	test = [[miCuenta.getNombre(), 'Ricardo'],
	[miCuenta.getApellidos(), 'Garrido'],
	[miCuenta.getDireccion(), 'Palma'],
	[miCuenta.getTelefono(), '617382654'],
	[miCuenta.getSaldo(), 120]]
	for miniTest in test:
		if miniTest[0]== miniTest[1]:
			print('ok test de los set y get de las propiedades de la clase')
		else:
			print('fail test de los set y get de las propiedades de la clase')
#test retirarDinero() ingresarDinero()
	miCuenta.setSaldo(0)
	miCuenta.ingresarDinero(100)
	if miCuenta.getSaldo() == 100:
		print ('ok test ingresarDinero()')
	else:
		print('fail test ingresarDinero()')
	miCuenta.retirarDinero(100)
	if miCuenta.getSaldo() == 0:
		print ('ok test retirarDinero()')
	else:
		print('fail test retirarDinero()')
# test saldoNegativo()
	tuCuenta=CuentaCorriente()
	tuCuenta.setSaldo(100)
	miCuenta.setSaldo(0)
	miCuenta.retirarDinero(100)
	test = [[miCuenta.saldoNegativo(), True],
	[tuCuenta.saldoNegativo(), False]]
	for miniTest in test:
		if miniTest[0]== miniTest[1]:
			print('ok test saldoNegativo')
		else:
			print('fail test saldoNegativo')


	miCuenta.consultarCuenta()

