"""Intro"""

MULTILINEA = """
Esto es 
una cadena
"""
NOMBRE = "Juan"
APELLIDO = "Perez"
NOMBRE_COMPLETO = NOMBRE + " " + APELLIDO
NOMBRE_COMPLETO2 = f"{NOMBRE} {APELLIDO}"

print("hola " * 4)  # imprime hola 4 veces
COMANDO = "hola"

print("\thola")  # tabulacion
print("hola\nmundo")  # salto de linea

print(COMANDO[0])  # primer caracter
print(len(COMANDO))  # longitud de la cadena
print(COMANDO[0:2])  # primeros dos caracteres
print(COMANDO[1:])  # desde el segundo caracter hasta el final
print(COMANDO[:3])  # desde el primer caracter hasta el tercero
print(COMANDO[-1])  # ultimo caracter
print(COMANDO[:])  # toda la cadena

print(NOMBRE.upper())  # todo mayusculas
print(NOMBRE.lower())  # todo minusculas
print(NOMBRE.title())  # primera letra de cada palabra mayuscula
print(NOMBRE.find("a"))  # posicion de la primera letra a
print("a" in NOMBRE)  # si existe la letra a
print(NOMBRE.replace("a", "e"))  # reemplazar a por e
print(NOMBRE.capitalize())  # primera letra mayuscula
print(NOMBRE.strip())  # quitar espacios en blanco al inicio y al final
print(NOMBRE.lstrip())  # quitar espacios en blanco al inicio
print(NOMBRE.rstrip())  # quitar espacios en blanco al final
