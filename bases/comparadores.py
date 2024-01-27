""" Operadores de comparacion"""
edad = 60

# Operadores de comparacion
# ==, !=, <, >, <=, >=

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


serie = "N-02"

match serie:
    case "N-01":
        print("Es la serie 1")
    case "N-02":
        print("Es la serie 2")
    case "N-03":
        print("Es la serie 3")
    case _:
        print("No es ninguna serie")
