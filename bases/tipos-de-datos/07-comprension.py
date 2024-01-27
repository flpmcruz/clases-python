usuarios = [
    ["Hector", 1],
    ["Juan", 2],
    ["Pedro", 3],
    ["Luis", 4],
    ["Ana", 5]
]

names = []
for user in usuarios:
    names.append(user[0])

# Lo mismo mas corto
nombres = [usuario[0] for usuario in usuarios]

print(names)
print(nombres)

# expresion for elemento in iterable if condicion
nombres2 = [usuario[0] for usuario in usuarios if usuario[1] % 2 == 0]
print(nombres2)


nombres3 = list(map(lambda usuario: usuario[0], usuarios))
menosUsuarios = list(filter(lambda usuario: usuario[1] % 2 == 0, usuarios))

# Si tiene else va antes del for
lista = [n if n % 2 == 0 else "No es par" for n in range(0, 11)]
print(lista)

# Si no tiene else va despues del for
valores = [1, 2, 3, 4, 5, 6, 9.5]
valores_pares = [n for n in valores if n % 2 == 0]


pies = [10, 20, 30, 40, 50]
metros = [pie * 0.3048 for pie in pies]
print(metros)
