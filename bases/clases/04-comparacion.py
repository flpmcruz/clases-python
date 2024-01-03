

class Coordenadas:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Este metodo se ejecuta cuando se usa el operador ==
    def __eq__(self, otro):
        return self.x == otro.x and self.y == otro.y

    def __ne__(self, otro):
        return not self.__eq__(otro)


coordenada1 = Coordenadas(10, 20)
coordenada2 = Coordenadas(10, 20)

print(coordenada1 == coordenada2)


# Si no definimos el metodo __eq__ se compara la referencia
# Si comparamos dos objetos que no son de la misma clase, se compara la referencia
coordenada3 = Coordenadas(10, 20)
otro_objeto = {'x': 10, 'y': 20}
