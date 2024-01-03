lista1 = [1, 2, 3, 4]
print(*lista1)  # desempaquetar la lista

lista2 = [5, 6, 7, 8]
lista3 = [*lista1, *lista2]
print(lista3)


punto1 = {"x": 1}
punto2 = {"y": 3}

puntos = {**punto1, **punto2}
print(puntos)
