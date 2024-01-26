"""Intro"""

MULTILINEA = """
Esto es 
una cadena
"""
NOMBRE = "Juan"
APELLIDO = "Perez"
NOMBRE_COMPLETO = NOMBRE + " " + APELLIDO
NOMBRE_COMPLETO2 = f"{NOMBRE} {APELLIDO}"
NOMBRE_COMPLETO3 = "Hola {} {}".format(NOMBRE, APELLIDO)

print("hola " * 4)  # imprime hola 4 veces
COMANDO = "hola"

print("\thola")  # tabulacion
print("hola\nmundo")  # salto de linea
print(len(COMANDO))  # longitud de la cadena

print(COMANDO[0])  # primer caracter
print(COMANDO[0:2])  # desde el primer caracter hasta el segundo
print(COMANDO[1:])  # desde el segundo caracter hasta el final
print(COMANDO[:3])  # desde el primer caracter hasta el tercero
print(COMANDO[-1])  # ultimo caracter
print(COMANDO[:])  # toda la cadena
print(COMANDO[0:2:2])  # desde el primer caracter hasta el segundo de 2 en 2
print(COMANDO[::2])  # desde el primer caracter hasta el ultimo de 2 en 2
print(COMANDO[::-1])  # invertir la cadena

print(NOMBRE.index("a"))  # posicion de la primera letra a
print(NOMBRE.index("a, 5, 10"))  # posicion de la primera letra a entre 5 y 10
print(NOMBRE.rindex("a"))  # posicion de la ultima letra a
print(NOMBRE.find("a"))
# posicion de la primera letra a. Si no existe devuelve -1 y no lanza error como index
print("a" in NOMBRE)  # si existe la letra a
print("a" not in NOMBRE)  # si no existe la letra a
print(NOMBRE.replace("a", "e"))  # reemplazar a por e
print(NOMBRE.count("a"))  # contar la cantidad de letras a
print(NOMBRE.startswith("J"))  # si empieza con J
print(NOMBRE.endswith("n"))  # si termina con n
print(NOMBRE.split("a"))  # separar por a
print(NOMBRE.split())  # separar por espacio
" ".join(["hola", "mundo"])  # unir por espacio

print(NOMBRE.upper())  # todo mayusculas
print(NOMBRE.lower())  # todo minusculas
print(NOMBRE.title())  # primera letra de cada palabra mayuscula
print(NOMBRE.capitalize())  # primera letra mayuscula
print(NOMBRE.swapcase())  # cambiar mayusculas por minusculas y viceversa

print(NOMBRE.strip())  # quitar espacios en blanco al inicio y al final
print(NOMBRE.lstrip())  # quitar espacios en blanco al inicio
print(NOMBRE.rstrip())  # quitar espacios en blanco al final
