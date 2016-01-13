class Fecha:
	def __init__(self, dia = 1, mes = 1, año = 1900):
		self.dia = dia
		self.mes = mes
		self.año = año
		self.diasMes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
		self.nombresMes = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']
		self.checkFecha()
	def setDia(self, dia):
		self.dia = dia
	def getDia(self):
		return self.dia
	def setMes(self, mes):
		self.mes = mes
	def getMes(self):
		return self.mes
	def setAño(self, año):
		self.año=año
	def getAño(self):
		return self.año
	def getDiasMes(self):
		return self.diasMes
	def getMesLetra(self):
		return self.nombresMes
	def mesLetra(self):
		return self.getMesLetra()[self.getMes()-1] 
	def setFecha(self, dia, mes, año):
			self.setDia(dia)
			self.setMes(mes)
			self.setAño(año)
			self.checkFecha()
	def getFecha(self):
		return '%s-%s-%s' %(self.getDia(),self.getMes(),self.getAño())
	def imprimirFecha(self):
		print('%s-%s-%s' %(self.getDia(),self.mesLetra(),self.getAño()))
	def incrementarFecha(self, dias):
		cantidadDias = self.getDia() + dias
		modificadorMes = -1
		modificadorAño = 0
		while cantidadDias > 0:
			if cantidadDias < self.diasMes[self.getMes() + modificadorMes]:
				self.setFecha(cantidadDias, self.getMes()+modificadorMes+1, self.getAño()+modificadorAño)
				break
			cantidadDias = cantidadDias - self.diasMes[self.getMes() + modificadorMes]
			if (self.getAño()+modificadorAño) % 4 == 0 and self.getMes()+modificadorMes == 1:
				cantidadDias -= 1
			modificadorMes += 1
			if self.getMes()+modificadorMes == 12:
				modificadorAño += 1
				self.setMes(1)
				modificadorMes = -1				
	def checkFecha(self):
		sano = False
		try:
			if self.getAño() > 1900 and self.getMes() in range(1,13) and self.getDia() in range(1, self.getDiasMes()[self.getMes()-1]+1):
				sano = True
			if self.getAño() >= 1900 and self.getMes() == 2 and self.getDia() == 29 and self.getAño() % 4 == 0:
				sano = True
		except:
			sano = False
		else:
			pass
		if sano == False:
				self.setDia(1)
				self.setMes(1)
				self.setAño(1900)
		else:
				pass
			
			
		
		
		
#test
if __name__ == '__main__':
	#test set y get
	cumpleaños = Fecha(29,6,1990)
	test=[[cumpleaños.getDia(),29],
		 [cumpleaños.getMes(),6],
		 [cumpleaños.getAño(),1990]]
	for miniTest in test:
		if miniTest[0]== miniTest[1]:
			print('ok test de los set y get de las propiedades de la clase')
		else:
			print('fail test de los set y get de las propiedades de la clase')
	#test check
	bisiesto = Fecha(29,2,2016)
	noBisiesto = Fecha (29,2,2017)
	tarado = Fecha ('tara','rara','ola')
	test=[[bisiesto.getDia(),29],
		 [bisiesto.getMes(),2],
		 [bisiesto.getAño(),2016],
		 [noBisiesto.getDia(),1],
		 [noBisiesto.getMes(),1],
		 [noBisiesto.getAño(),1900],
				 [tarado.getDia(),1],
		 [tarado.getMes(),1],
		 [tarado.getAño(),1900]]
	for miniTest in test:
		if miniTest[0]== miniTest[1]:
			print('ok test de check')
		else:
			print('fail test de check')
	#test setFecha
	cumpleaños.setFecha(5,5,1987)
	test=[[cumpleaños.getDia(),5],
		 [cumpleaños.getMes(),5],
		 [cumpleaños.getAño(),1987]]
	for miniTest in test:
		if miniTest[0]== miniTest[1]:
			print('ok test set Fecha')
		else:
			print('fail test set Fecha')
	#test incremetar Fecha
	cumpleaños.setFecha(28,2,1988)
	cumpleaños.incrementarFecha(365)
	test=[[cumpleaños.getDia(),27],
		 [cumpleaños.getMes(),2],
		 [cumpleaños.getAño(),1989]]
	for miniTest in test:
		if miniTest[0]== miniTest[1]:
			print('ok test de incrementar Fecha')
		else:
			print('fail test de incrementar Fecha')
	#test mesLetra
	cumpleaños.setFecha(2,2,1988)
	if cumpleaños.mesLetra() == 'Febrero':
		print('ok test mes letra')
	else:
		print('fail test mes letra')
	if cumpleaños.getFecha() == '2-2-1988':
		print('ok test get Fecha')
	else:
		print('Fail test get Fecha')
	cumpleaños.imprimirFecha()	
		      
	
	
	
	
