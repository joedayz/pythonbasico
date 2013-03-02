nombres = []
ramas = []
total_ramas = 0
for i in range(2):
	nombre = raw_input('ingresa nombre: ')
	cant_ramas = raw_input('ingresa cantidad de ramas: ')
	nombres.append(nombre)
	total_ramas = total_ramas + int(cant_ramas)
	ramas.append(int (cant_ramas))

for j in range(2):
	print nombres[j] + " --> " + str(ramas[j]*100.0/total_ramas + 'soles')
	
