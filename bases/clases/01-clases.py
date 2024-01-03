
class MiPerro:
    patas = 4

    # El método __init__ es el constructor de la clase
    def __init__(self, nombre, edad):
        # Los atributos privados se definen con doble guión bajo al inicio
        self.__nombre = nombre
        self.edad = edad

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def saludar(self):
        print("Hola me llamo", self.__nombre, "y tengo", self.edad, "años")

    # Los métodos de clase se definen con el decorador @classmethod
    @classmethod
    def ladrar(cls):
        print("Guau Guau")

    # Se pueden usar métodos de clase para crear instancias de la clase
    @classmethod
    def factory(cls, nombre, edad):
        return cls(nombre, edad)


MiPerro.ladrar()
perro1 = MiPerro("Firulais", 5)
perro1.ladrar()

perro2 = MiPerro.factory("Scooby", 10)
perro2.saludar()


# isinstance() es una función que nos permite saber si un objeto es instancia de una clase
print(isinstance(perro1, MiPerro))

# hasattr() es una función que nos permite saber si un objeto tiene un atributo
print(MiPerro.patas)
