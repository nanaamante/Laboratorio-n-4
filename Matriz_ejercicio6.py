#6. Calcular la determinante de una matriz
import numpy as np

print("Ingrese el orden de la matriz a calcular: ")
filasM, columnasM = int(input()), int(input())

contador = 0

if columnasM == filasM:
    
    matrizM = []
    for i in range (filasM):
        matrizM.append([0]*columnasM)
    
    print("Ingrese la matriz M ")
    for fila in range(filasM):
        for columna in range(columnasM):
            matrizM[fila][columna] = float(input(f"Ingrese la posición número {fila}, {columna}: "))
        
#Hallar determinante
determinante = np.linalg.det(matrizM)
print(determinante)