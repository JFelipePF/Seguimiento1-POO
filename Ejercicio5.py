# -*- coding: utf-8 -*-
"""
Created on Tue Sep  9 11:48:56 2025

@author: 65681
"""

#Ejercicio 5
import math as math
class CalculosEj5:
    def CalSuma(SUMA, X):  
        return SUMA + X
    
    def CalX(X,Y):
        return X + math.pow(Y,2)
class Ejercicio5:
    def main():
        SUMA = float(input('Ingrese un valor para SUMA:'))
        X = float(input('Ingrese un valor para X:'))
        Y = float(input('Ingrese un valor para Y:'))
        SUMA = CalculosEj5.CalSuma(SUMA, X)
        X = CalculosEj5.CalX(X, Y)
        SUMA = SUMA + X / Y
        print('El valor de la SUMA es:', SUMA)
if __name__ == " __main__ " :
    Ejercicio5.main()  