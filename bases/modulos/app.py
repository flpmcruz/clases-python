from usuarios.acciones import bailar, cantar

bailar()
cantar()

# la diferencia entre un modulo y un paquete es que un paquete es un conjunto de modulos. Un modulo es un archivo .py y un paquete es una carpeta que contiene modulos.
# Para que una carpeta sea un paquete debe contener un archivo __init__.py

# Otra forma: importar el modulo del paquete
# import usuarios.acciones
# usuarios.acciones.cantar()

# Otra forma: importar el modulo del paquete
# from usuarios import acciones
# acciones.cantar()


# uso del dir
# print(dir(usuarios.acciones))
