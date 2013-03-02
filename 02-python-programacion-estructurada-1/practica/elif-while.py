#Escribe un programa que pregunte primero si quieres calcular el área de un triángulo 
#o de un círculo. Dependiendo de la respuesta el programa debe pedir la base y la altura, 
#o el radio, para calcular el área de la figura.

while 1:
    print """
    Opcion:
    1 - Calcular area de un triangulo
    2 - Calcular area de un circulo
    3 - Salir
           """
    Opc = input("Numero de la opcion > ")
    if Opc == 1:
        bBase = input("Base > ")
        hAltura = input("Altura > ")
        print "Solucion: %d" % (bBase * hAltura / 2)
    elif Opc == 2:
        PI = 3.14
        rRadio = input("Radio > ")
        print "Solucion: %d" % (PI * rRadio * rRadio)
    else:
        exit()