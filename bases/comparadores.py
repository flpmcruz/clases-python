""" Operadores de comparacion"""
edad = 60

if edad >= 54:
    print("Puedes ver la pelicula con descuento")
elif edad > 17:
    print("Puedes ver peliculas para mayores de 17")
else:
    print("No puedes entrar")

mensaje = "Es mayor" if edad >= 18 else "Es menor"
print(mensaje)


# Operadores logicos and, or, not
gas = False
encendido = True

if gas and encendido:
    print("Puedes avanzar")

print("Fin del programa")
