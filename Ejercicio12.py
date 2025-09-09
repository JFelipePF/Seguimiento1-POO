   #Ejercicio 12

class CalculosEj12:   
    def salBruto(horas_laboradas, precio_hora):
        salario_bruto = horas_laboradas * precio_hora
        return salario_bruto
    
    def porcRet(retencion):
        porcentaje_retencion = retencion / 100
        return porcentaje_retencion
    
    def retFuente(porcentaje_retencion, salario_bruto):
        retencion_fuente = porcentaje_retencion * salario_bruto
        return retencion_fuente
    
    def salNeto(salario_bruto,retencion_fuente):
        salario_neto = salario_bruto - retencion_fuente
        return salario_neto}
        
class Ejercicio12:
    def main():
        salario = float(input('Ingrese su salario en $:'))
        Horas = float(input('Ingrese las horas laboradas:'))
        retencion = float(input('Ingrese la retención:'))
        salario_bruto = CalculosEj12.salBruto(salario,Horas)
        porc_retencion = CalculosEj12.porcRet(retencion)
        retencion_fuente = CalculosEj12.retFuente(porc_retencion,salario_bruto)
        salario_neto = CalculosEj12.salNeto(salario_bruto,retencion_fuente)
        print('El salarion neto es:', salario_neto)
if __name__ == " __main__ " :
    Ejercicio12.main() 
