class Hora:
	def __init__(self, hora = 0, minutos = 0, segundos = 0):		
		self.hora = hora
		self.minutos = minutos
		self.segundos = segundos
		self.checkHora()
		self.checkMinutos()
		self.checkSegundos()
	def checkHora(self):
		if 0<=self.getHoras()<=24:
			pass
		else:
			self.setHoras(0)
	def checkMinutos(self):
		if 0<=self.getMinutos()<60:
			pass
		else:
			self.setMinutos(0)
	def checkSegundos(self):
		if 0<=self.getSegundos()<60:
			pass
		else:
			self.setSegundos(0)
	def setHoras(self, hora):
		self.hora = hora
		self.checkHora()
	def getHoras(self):
		return self.hora
	def setMinutos(self, minutos):
		self.minutos = minutos
		self.checkMinutos()
	def getMinutos(self):
		return self.minutos
	def setSegundos(self, segundos):
		self.segundos = segundos
		self.checkSegundos()
	def getSegundos(self):
		return self.segundos
	def setHora(self, hora, minutos, segundos):
		self.setHoras(hora)
		self.setMinutos(minutos)
		self.setSegundos(segundos)
		self.checkHora()
		self.checkMinutos()
		self.checkSegundos()
	def getHora(self):
		return '%s:%s:%s' %(self.getHoras(),self.getMinutos(),self.getSegundos())
	def imprimirHora(self):
		print(self.getHora())
#test

if __name__ == '__main__':
#test set y get
	japon = Hora()
	test = [[japon.getHoras(), 0 ],
		[japon.getMinutos(), 0],
		[japon.getSegundos(), 0],
		[japon.getHora(),'0:0:0']]
	for miniTest in test:
		if miniTest[0]== miniTest[1]:
			print('ok test de los set y get de las propiedades de la clase')
		else:
			print('fail test de los set y get de las propiedades de la clase')
	
		
	japon.setHoras(1)
	japon.setMinutos(1)
	japon.setSegundos(1)
	test = [[japon.getHoras(), 1 ],
		[japon.getMinutos(), 1 ],
		[japon.getSegundos(), 1 ]]
	for miniTest in test:
		if miniTest[0]== miniTest[1]:
			print('ok test de los set y get de las propiedades de la clase')
		else:
			print('fail test de los set y get de las propiedades de la clase')
	japon.setHora(2,2,2)
	if japon.getHora()== '2:2:2':
		print('ok test de los set y get de las propiedades de la clase')
	else:
		print('fail test de los set y get de las propiedades de la clase')
#test check
	japon.setHoras(100)
	japon.setMinutos(100)
	japon.setSegundos(100)
	test = [[japon.getHoras(), 0 ],
		[japon.getMinutos(), 0],
		[japon.getSegundos(), 0],
		[japon.getHora(),'0:0:0']]
	for miniTest in test:
		if miniTest[0]== miniTest[1]:
			print('ok test check')
		else:
			print('fail test check')
	
	
	
	
	
