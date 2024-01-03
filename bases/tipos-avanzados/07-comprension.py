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
