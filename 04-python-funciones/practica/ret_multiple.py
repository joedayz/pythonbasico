#crea una funcion que al ingresar una cadena verifique si es un palindromo
#usando retornos multiples te debe devolver la cadena ingresada, la cadena invertida y 
#valor de verdad( True si son iguales, y False si son diferente)

def palindrome(cad):
	valor = False
	aux = ""
	for i in range(len(cad)-1, -1 ,-1):
		aux = aux + cad[i]
	
	if cad==aux:
		valor = True
		
	return cad,valor,aux
	
cad = raw_input('Ingrese cadena-->')
cadena,valor,aux = palindrome(cad)

if valor==True:
	print "la cadena " + cadena + " es un palindromo " 
else:
	print "la cadena " + cadena + " no es un palindromo " 
