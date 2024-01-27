from random import *

numero = randint(1, 100)
intentos = 0
adivinanza = 0

while intentos < 8:
    print("Adivina el número entre 1 y 100")
    adivinanza = input()
    adivinanza = int(adivinanza)

    intentos += 1

    if adivinanza < numero:
        print(f"Muy bajo, llevas {intentos} intentos, ¡sigue intentando!")
    if adivinanza > numero:
        print(f"Muy alto llevas {intentos} intentos, ¡sigue intentando!")
    if adivinanza == numero:
        print(f"¡Felicidades! ¡Has adivinado el número en {
            intentos} intentos!")
        break

if adivinanza != numero:
    print("Lo siento, no has adivinado el número. El número era " + str(numero))
