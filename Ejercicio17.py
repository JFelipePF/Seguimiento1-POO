# Ejercicio 17
import math as math
class CalculosEj17:
    def area(r):
        return math.pi * math.pow(r, 2)
    def perimetro(r):
        return 2 * math.pi * r
class Ejercicio17:
    def main():
        r = float(input('Ingrese el radio de la circunferencia:'))
        print('El area de la circunferencia es:', CalculosEj17.area(r))
        print('El perimetro o la longitud de la circunferencia es:', CalculosEj17.perimetro(r))
if __name__ == " __main__ " :
    Ejercicio17.main()  
