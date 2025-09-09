#Ejercicio 14

class CalculosEj14:
    def cuadrado(num):
        return num ** 2
    def cubo(num):
        return num ** 3

class Ejercicio14:
    def main():
        num = float(input('Ingrerse un número:'))
        print(f'El número seleccionado es {num}')
        print('El cuadrado del número es:', CalculosEj14.cuadrado(num))
        print('El cubo del número es:', CalculosEj14.cubo(num))
if __name__ == " __main__ " :
    Ejercicio14.main() 
