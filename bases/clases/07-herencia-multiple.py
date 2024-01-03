
class Animal:
    def comer(self):
        print("El animal está comiendo")

    def pasear(self):
        print("El animal está paseando")

# La clase Perro hereda de la clase Animal


class Perro:
    def pasear(self):
        print("El perro está paseando")

# El orden es importante porque si hay metodos que se llaman igual, se va a ejecutar el primero que se encuentre


class Chanchito(Perro, Animal):
    def programar(self):
        print("El chanchito está programando")


chanchito = Chanchito()
chanchito.pasear()
