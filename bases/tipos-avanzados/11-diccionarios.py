
# las llaves tienen que ser strings
punto = {
    "x": 10,
    "y": 20
}

print(punto["x"])
print(punto["y"])

# agregar un nuevo elemento
punto["z"] = 30

if "z" in punto:
    print("Si esta en el diccionario")


print(punto.get("a", 0))  # si no existe la llave, devuelve 0


del punto["x"]  # elimina la llave x y su valor


for key in punto:
    print(key, punto[key])


for key, value in punto.items():
    print(key, value)


usuarios = [
    {"id": 1, "nombre": "Juan"},
    {"id": 2, "nombre": "Pedro"},
    {"id": 3, "nombre": "Pablo"},
    {"id": 4, "nombre": "Luis"},
    {"id": 5, "nombre": "Maria"}
]

for usuario in usuarios:
    print(usuario["id"], usuario["nombre"])
