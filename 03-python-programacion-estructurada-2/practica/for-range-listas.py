#Numeros amigos
#Dos números amigos son dos enteros positivos a y b tales 
#que a es la suma de los divisores propios de b, y b es la 
#suma de los divisores propios de a. (la unidad se considera 
#divisor propio, pero no lo es el mismo número).

n1 = input('Introduzca el n 1: ')
n2 = input('Introduzca el n 2: ')

suma_n1=0
suma_n2=0
for i in range(1,n1):
    if n1%i==0:
       suma_n1+=i
 
for k in range(1,n2):
    if n2%k==0:
       suma_n2+=k
 
 
 
if (suma_n1==n2 and suma_n2==n1):
    print ('Son amigos :)')
else:
    print ('No son amigos :(')
