numeros = [1, 2, 3]
letras = ["a", "b", "c"]
ceros = [0] * 10

alfanumerico = numeros + letras

# list crea una lista a partir de un iterable
rango = list(range(10))  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
rango2 = list(range(1, 11))  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
rango3 = list("Hola")  # ['H', 'o', 'l', 'a']

mascotas = ["perro", "gato", "pez", "conejo", "elefante", "hormiga"]

print(mascotas[0])  # "perro"
print(mascotas[-1])  # "hormiga" (último elemento)
print(mascotas[1:3])  # ["gato", "pez"]
print(mascotas[:3])  # ["perro", "gato", "pez"]
print(mascotas[3:])  # ["conejo", "elefante", "hormiga"]
print(mascotas[::2])  # ["perro", "pez", "elefante"] elementos de 2 en 2
