
# los metodos magicos son metodos que se ejecutan automaticamente
# Son metodos que se reciben por herencia

class Perro:
    def __init__(self, nombre):
        self.nombre = nombre

    # Este metodo se ejecuta cuando se imprime el objeto o cuando se convierte a string
    def __str__(self):
        return f"Perro: {self.nombre}"

    def __del__(self):
        print(f"El perro {self.nombre} ha sido eliminado")

    # def __len__(self):
    #     return len(self.nombre)


perro = Perro("Firulais")
del perro
