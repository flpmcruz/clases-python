
class Animal:
    def comer(self):
        print("El animal está comiendo")

# La clase Perro hereda de la clase Animal


class Perro(Animal):
    def pasear(self):
        print("El perro está paseando")


class Chanchito(Perro):
    def programar(self):
        print("El chanchito está programando")


chanchito = Chanchito()
chanchito.pasear()
