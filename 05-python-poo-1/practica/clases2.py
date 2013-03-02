class Persona:
    # atributos

    nombre = ""
    edad = 0
 
    # metodos

    def setNombre(self, x):
        self.nombre = x


    def setEdad(self, x):
        self.edad = x
 

    def talk(self):
		print "hola tu nombre es " + self.nombre + " y tienes " + str(self.edad) + " anios de edad"

myObject = Persona()
nom = raw_input('Ingresa tu Nombre --> ')
edad = raw_input('Ingresa tu edad --> ')
myObject.setNombre(nom)
myObject.setEdad(edad)
myObject.talk()
