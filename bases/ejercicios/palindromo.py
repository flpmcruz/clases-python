

def print_palindromo(palabra):
    """Imprime si una palabra es palíndromo o no.

    Parámetros:
    palabra -- palabra a evaluar
    """
    if palabra == palabra[::-1]:
        print("La palabra es palíndromo")
    else:
        print("La palabra no es palíndromo")


def main():
    """Función principal."""
    palabra = input("Ingrese una palabra: ")
    print_palindromo(palabra)


if __name__ == "__main__":
    main()
