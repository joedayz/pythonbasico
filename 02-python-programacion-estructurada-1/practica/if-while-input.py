##Introducir los valores A, B y C: 
###Si A/B>30, calcular e imprimir A/C * B^3 
###Si A/B<=30, calcular e imprimir 2^2+4^2+6^2+...+30^2

#a = raw_input('Primer valor: ')
#b = raw_input('Segundo valor: ')
#c = raw_input('Tercer valor: ')

a=60.0
b=1
c=6
n = 2
suma1 = 0
suma2 = 0

if a/b > 30:
    suma1 = (a/c)*b**3
    print suma1
elif a/b <= 30:
    while n <= 30:
        suma2 += n**2
        n += 2
    print suma2