#3. Calcular la diagonal principal de una matriz
import numpy as np 

print("Ingrese el orden de la matriz a calcular: ")
filasM, columnasM = int(input()), int(input())

diagonal = 0

if filasM == columnasM:
    #creando la matriz vacia
    matrizM = []
    for i in range (filasM):
        matrizM.append([0]*columnasM)
    #rellenando la matriz
    print("Ingrese la matriz M ")
    for fila in range(filasM):
        for columna in range(columnasM):
            matrizM[fila][columna] = float(input(f"Ingrese la posición número {fila}, {columna}: "))
    #calculando la matriz diagonal principal de la matriz A
    for fila in range(filasM):
        for columna in range(columnasM):
            if fila == columna:
                diagonal += matrizM[fila][columna]
    
    
    print(f"El valor de la diagonal principal es: {diagonal} ")