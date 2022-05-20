import numpy as np

lista = [1,2,3,4,5,6,7,8]
arreglo=np.array(lista)
print(type(arreglo))
matriz = [[1,2,3],[4,5,6],[7,8,9]]
matriz = np.array(matriz)
print(matriz)

print(lista[1])
print(matriz[2,2])
print(matriz[1:,0:2])