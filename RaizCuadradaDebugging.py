# -*- coding: utf-8 -*- 

import math


def raizcuadrada(x, eps = 10e-7):
        #Precondición
	assert x >= 0, "x debe ser mas grande que 0"

	b = x
	fin = False

	if b == 0:
		return b
	else:
		fin = False
		while not fin:
			if abs(b * b - x) < eps: #epsilon
				return b
			else:
				b = (1/2)*(x/b + b)
	#Postcondición			
	assert x == b * b


def test():

	print("Introduce x")
	x = float(input('x = '))
	# raw_input devuelve un string

	print(raizcuadrada(x))


test()



"""
Pasos Debugging

--> Al ejecutar la aplicación nos da un TypeError, que el valor introducido devolvia un string.
--> Podemos intuir que una raiz cuadrada menor a 0 no existe, 
    por lo que el programa no funcionaria. Uso de una precondición (assert x > 0) y postcondición (assert x == b * b)
--> Utilización de Epsilon para arreglar la precisión del resultado

"""
