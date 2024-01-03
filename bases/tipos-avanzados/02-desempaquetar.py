numeros = [1, 2, 3]

# Desempaquetar una lista (es como desectructurar un objeto en JavaScript)
primero, segundo, tercero = numeros

print(primero)  # 1
print(segundo)  # 2
print(tercero)  # 3

n1, n2, *resto = numeros  # resto es una lista con el resto de elementos

nn1, *resto, nn2 = numeros  # el primero, el resto y el último
