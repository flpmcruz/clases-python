numeros = [1, 5, 2, 4, 3]

numeros.sort()  # ordena la lista
numeros.sort(reverse=True)  # ordena la lista en reversa

sorted(numeros)  # ordena la lista y retorna una nueva lista
# ordena la lista en reversa y retorna una nueva lista
sorted(numeros, reverse=True)


usuarios = [
    [4, "Juan"],
    [2, "Pedro"],
    [3, "Luis"],
    [1, "Ana"],
]
usuarios.sort()  # ordena la lista por el primer elemento de cada sublista


usuarios2 = [
    ["Juan", 4],
    ["Pedro", 2],
    ["Luis", 3],
    ["Ana", 1]
]


def ordenar_por_edad(usuario):
    return usuario[1]


# ordena la lista por el segundo elemento de cada sublista
usuarios2.sort(key=ordenar_por_edad)

# lo mismo que la función anterior pero usando una función lambda
usuarios2.sort(key=lambda usuario: usuario[1])
