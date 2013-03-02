#yo traia a mis 4 sobrinos y sobrinas a mi casa de playa en verano para 
#recoger las malas hierbas, ya que odio hacerlo yo mismo.He pagado $12.50
#a cada uno de ellos para que me ayude a recoger, pero me he molestado ya 
#que no lo hacen como deben y se pasan el tiempo haciendo otras cosas.
#He decidido que el proximo verano pagare $100 en total pero esta vez cada
#persona recibira de acuerdo a su trabajo. Necesito tu programa para que el 
#usuario escriba 4 nombres de los niños y el número de malezas cada uno de 
#los chicos recogio luego imprimir una lista de la cantidad de cada niño se 
#ha ganado. 
#El porcentaje de la $ 100 que reciben deben basarse en el porcentaje de la 
#pila de malas hierbas que se recogió

nombres = {}
total_ramas = 0
for i in range(2):
	nombre = raw_input('ingresa nombre: ')
	cant_ramas = raw_input('ingresa cantidad de ramas: ')
	total_ramas = total_ramas + int(cant_ramas)
	nombres[nombre] = int(cant_ramas)	
 

for nom in nombres.keys():
	nombres[nom] = nombres[nom]*100.0/total_ramas
	print nom + ' --> ' + str(nombres[nom]) 
	
