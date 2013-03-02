#Dado un conjunto de coeficientes hallar P(x) siendo un polinomio
#P(x) = a0 + a1.x + a2.x^2 + a3.x^3 + ..... + an.x^n



class Polinomio:

    def __init__(self, coefficients):
      
        self.coefficients = coefficients

    def evaluar(self, x):
        y = 0
        for i, a in enumerate(self.coefficients):
            y += a * x**i  
        return y


data = [2, 1, 3]
p = Polinomio(data)  # crea la instancia del polinomio
n = raw_input('Ingrese numero --> ')
resultado = p.evaluar(int(n))
print "El polinomio P("+ str(n)+")" + " = " + str (resultado)

