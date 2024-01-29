from random import choice

palabras = ["arbol", " bicicleta"]
palabra_elegida = choice(palabras)
palabra_en_guiones = "_" * (len(palabra_elegida) - 1)
letras_incorrectas = []
VIDAS = 6


def llenar(letra):
    global VIDAS
    global palabra_en_guiones
    if letra in palabra_elegida:
        # llenar letras en palabra con guiones
        print("vas bien")
        indices = [i for i, char in enumerate(
            palabra_elegida) if char == letra]
        indices = [i-1 for i in indices]

        print(indices)

        lista = list(palabra_en_guiones)
        for n in indices:
            lista[n] = letra

        nueva = ''
        for l in lista:
            nueva += l

        print(lista)
        palabra_en_guiones = nueva

    else:
        letras_incorrectas.append(letra)
        VIDAS -= 1


while VIDAS > 0 and palabra_en_guiones != palabra_elegida:
    print(f"Tienes {VIDAS} vidas")
    print(f"La palabra es: {palabra_en_guiones}")
    letra = input("Elija una letra para comenzar: ")

    # Validar letra
    llenar(letra)

    print(f"Letras incorrectas: {letras_incorrectas}")
    print(palabra_en_guiones)


if palabra_en_guiones == palabra_elegida:
    print("Felicitaciones")
else:
    print("Lo siento, intenta de nuevo")
