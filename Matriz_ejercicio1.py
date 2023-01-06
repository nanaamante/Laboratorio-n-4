#Suma, resta, multiplicación de matrices.
import numpy as np

M = np.array([[1,2,3,4,5],[6,7,8,9,0]])
N = np.array([[3,2,0,4,3],[0,2,1,7,4]])

suma_Matrices = M + N
print(M)
print(N)
print("La suma de matrices es:\n", suma_Matrices)

#Resta
M = np.array([[1,2,3,4,5],[6,7,8,9,0]])
N = np.array([[3,2,0,4,3],[0,2,1,7,4]])

resta_Matrices = M - N
print(M)
print(N)
print("La resta de matrices es:\n", resta_Matrices)

#Multiplicación
M = np.array([[1,2,3,4],[6,7,8,9]])
N = np.array([[3,2,0,4],[0,2,1,7]])

multiplicacion_Matrices = M * N
print(M)
print(N)
print("La multiplicación de matrices es:\n", multiplicacion_Matrices)

