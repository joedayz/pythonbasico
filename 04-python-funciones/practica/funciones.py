
#Escribir un function car_freq() que toma una cadena y cree una lista de frecuencia de los 
#caracteres contenidos en el mismo. Representar a la indicación de frecuencia como un diccionario de Python. 
#Prueba con algo como char_freq ("abbabcbdbabdbdbabababcbcbab").

def car_freq(cad):
	d={}
	for i in cad:
		if i not in d:
			d[i]=0
		d[i]+=1
	
print d
	
cad = raw_input('Ingrese cadena->')
		
car_freq(cad)


