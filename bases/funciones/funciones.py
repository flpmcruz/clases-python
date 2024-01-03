
def hola(nombre, apellido="Mireles"):
    print(f"Hola {nombre} {apellido}")


hola("Juan")
hola("Pedro", "Perez")
hola(apellido="Perez", nombre="Pedro")  # Argumentos nombrados
hola("Pedro", apellido="Perez")  # Argumentos posicionales y nombrados
