# SERIE TAYLOR
import os
import math
try:
                num = int(
                    input("Digita un numero para obtener la solucion de la serie: "))
                dato = 0
                os.system('cls')
                for i in range(0, num + 1):
                    dato += (math.pow(5, i) / math.factorial(i))
                print('Respuesta de la serie: ', dato)
except:
                 print('Error dato invalido')
# SENO Y COSENO
try:
                n = int(input("Digita el valor de n: "))
                x = int(input("Digita el valor de x: "))

                sen = math.pow(-1, n) * (math.pow(x, 2*n+1) /
                                         math.factorial(2*n+1))
                cos = math.pow(-1, n) * (math.pow(x, 2*n) /
                                         math.factorial(2*n))

                print('SENO: ', sen)
                print('COSENO: ', cos)
except:
                print('Error dato invalido')