nombres = ["Juan", "Karla", "Ricardo", "María"]
for nombre in nombres:
    print(nombre)

for nombre in enumerate(nombres):
    print(nombre)  # Imprime tuplas con indice y valor


buscar = 3
for numero in range(5):
    if numero == buscar:
        print("Encontrado", numero)
        break
else:
    print("No encontrado")

# Iterar sobre una lista
for char in "Character":
    print(char)


# While loop
numero = 0
while numero < 5:
    print(numero)
    numero += 1


comando = ""
while comando.lower() != "salir":
    comando = input(">")
    print("Escribiste", comando)


# while True:
#     comando = input(">")
#     if comando.lower() == "salir":
#         break
#     print("Escribiste", comando)
