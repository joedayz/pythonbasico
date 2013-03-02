#Metodos de Listas

lista = ['Peru','Brazil','Colombia','Argentina','Ecuador']
print "lista --> ",lista

print "lista[1] --> ",lista[1]
lista[1:3] = ['xxx', 'yyy']
print "lista[1:3] = ['xxx', 'yyy'] --> ", lista

del lista[1:3]
print "del lista[1:3] --> ",lista

print "max(lista) --> ",max(lista)
print "min(lista) --> ",min(lista)

lista.append('Nicaragua')
print "lista.append('Nicaragua') --> ",lista

lista.reverse()
print "lista.reverse() --> ",lista
print "id(list) --> ",id(lista)
