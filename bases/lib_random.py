from random import *

aleatorio = randint(0, 10)
print(aleatorio)

aleatorio2 = round(uniform(0, 10), 2)
print(aleatorio2)

aleatorio3 = choice(['Carlos', 'Juan', 'Pedro'])
print(aleatorio3)

aleatorio4 = random()
print(aleatorio4)

numeros = list(range(0, 51, 5))
shuffle(numeros)  # Mezcla los elementos de la lista, modificando la lista original
print(numeros)
