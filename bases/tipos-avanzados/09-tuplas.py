# Las tuplas son inmutables, se pueden hacer las mismas operaciones que con las listas pero no se pueden modificar
numeros = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(numeros[0])

# crear una lista a partir de una tupla
numeros2 = list(numeros[:])
print(numeros2)


# crear una tupla a partir de una lista
numeros3 = tuple(numeros2)
print(numeros3)
