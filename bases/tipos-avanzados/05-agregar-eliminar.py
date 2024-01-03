mascotas = ["perro", "gato", "pez", "conejo", "elefante", "hormiga"]

mascotas.insert(2, "tortuga")
mascotas.append("tortuga")

# elimnar
mascotas.remove("tortuga")
mascotas.pop()  # elimina el último elemento
mascotas.pop(2)  # elimina el elemento en el índice 2
del mascotas[0]  # elimina el elemento en el índice 0

mascotas.clear()  # elimina todos los elementos
