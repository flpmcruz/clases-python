from io import open

# ESCRIBIR UN ARCHIVO
# texto = "Hola mundo"

# # si no existe el archivo lo crea
# archivo = open("archivos/archivo.txt", "w")

# archivo.write(texto)
# # es necesario cerrar el archivo para que no se quede en memoria
# archivo.close()

# agregar texto a un archivo
# archivo = open("archivos/archivo.txt", "a+")
# archivo.write("\nChao mundo")
# archivo.close()

# LEER UN ARCHIVO
# por defecto el modo es lectura, no es necesario poner r

# archivo = open("archivos/archivo.txt", "r")
# texto = archivo.read()
# archivo.close()
# print(texto)

# lectura como lista
# archivo = open("archivos/archivo.txt", "r")
# lineas = archivo.readlines()
# archivo.close()
# print(lineas)

# ------------------------------------------------------------
# Otra forma de hacerlo para no tener que cerrar el archivo
# Si trabajamos con with no es necesario cerrar el archivo

# with and seek
# with open("archivos/archivo.txt", "r") as archivo:
#     # lee todas las lineas y las guarda en una lista
#     print(archivo.readlines())
#     archivo.seek(0)  # posiciona el cursor en el caracter 0
#     for linea in archivo:
#         print(linea)


# lectura y escritura
with open("archivos/archivo.txt", "r+") as archivo:
    texto = archivo.readlines()
    archivo.seek(0)
    texto[0] = "Esta linea ha sido modificada en memoria\n"
    archivo.writelines(texto)
