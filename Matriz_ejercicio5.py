#5. Hallar la matriz simétrica
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

    
    for fila in range(filasM):
        for columna in range(columnasM):
            normal=matrizM[fila][columna]
            transpuesta=matrizM[columna][fila]
            if normal == transpuesta:
                contador += 1
    

    
    if contador ==(filasM*columnasM):
        print("La matriz SÍ es simétrica")
    else:
        print("La matriz NO es simétrica")
else:
    print("La matriz no es simétrica")