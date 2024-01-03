

class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def __str__(self):
        return f'{self.nombre} - ${self.precio}'


class Categoria:
    productos = []

    def __init__(self, nombre, productos):
        self.nombre = nombre
        self.productos = productos

    def agregar(self, producto):
        self.productos.append(producto)

    def imprimir(self):
        print(f'Categoria: {self.nombre}')
        for producto in self.productos:
            print(producto)


kayak = Producto('Kayak', 17000)
pelota = Producto('Pelota', 500)
bicicleta = Producto('Bicicleta', 20000)
deportes = Categoria('Deportes', [kayak, pelota])

deportes.agregar(bicicleta)
deportes.imprimir()
