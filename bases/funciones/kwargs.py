# el ** indica que se recibiran varios argumentos y se guardaran en un diccionario
def listar_terminos(**kwargs):
    for llave, valor in kwargs.items():
        print(f"{llave}: {valor}")  # items() regresa una lista de tuplas

    print(kwargs["IDE"])  # Acceder a un elemento del diccionario


listar_terminos(IDE="Integrated Development Environment", PK="Primary Key")
