numeros = [1, 2, 3]
letras = ["a", "b", "c"]
ceros = [0] * 10

alfanumerico = numeros + letras  # [1, 2, 3, "a", "b", "c"]

# list crea una lista a partir de un iterable
rango = list(range(10))  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
rango2 = list(range(1, 11))  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
rango3 = list("Hola")  # ['H', 'o', 'l', 'a']

mascotas = ["perro", "gato", "pez", "conejo", "elefante", "hormiga"]

print(len(mascotas))  # 6

# Acceso a elementos igual que en cadenas de texto
print(mascotas[0])  # "perro"
print(mascotas[-1])  # "hormiga" (último elemento)
print(mascotas[1:3])  # ["gato", "pez"]
print(mascotas[:3])  # ["perro", "gato", "pez"]
print(mascotas[3:])  # ["conejo", "elefante", "hormiga"]
print(mascotas[::2])  # ["perro", "pez", "elefante"] elementos de 2 en 2

# Los strings son inmutables, las listas no
mascotas[0] = "gato"  # sustituye "perro" por "gato"

mascotas.append("perro")  # añade "perro" al final de la lista
mascotas.insert(0, "perro")  # añade "perro" en la posición 0
mascotas.remove("perro")  # elimina la primera ocurrencia de "perro"
del mascotas[0]  # elimina el elemento en el índice 0
mascotas.pop()  # elimina el último elemento de la lista y lo devuelve
mascotas.pop(0)  # elimina el elemento en la posición 0 y lo devuelve
mascotas.clear()  # vacía la lista


lista = ["g", "a", "t", "o"]
numeros = [1, 5, 2, 4, 3]

lista.reverse()  # ["o", "t", "a", "g"]
numeros.reverse()  # [3, 4, 2, 5, 1]
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
