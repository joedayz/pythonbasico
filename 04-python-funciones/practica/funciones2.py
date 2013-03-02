#Decir si un numero es perfecto o no. Un Numero es perfecto si es la suma de todos sus divisores
#sin incluir a el. Ej. 6 = 1 + 2 + 3


def es_perfecto(n):
	sumatorio = 0
	for i in range(1, n):
		if n % i == 0:
			sumatorio += i
	if sumatorio == n:
		return 1
	else:
		return 0

if es_perfecto(6):
	print "Es Perfecto"
else:
	print "No es Perfecto"
