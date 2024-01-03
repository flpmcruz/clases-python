
def limpiar(texto):
    cadena = ""
    for char in texto:
        if char != " ":
            cadena += char
    return cadena


def reverse(texto):
    cadena = ""
    for char in texto:
        cadena = char + cadena
    return cadena


def is_palindromo(text):
    text_sin_espacios = limpiar(text)
    texto_invertido = reverse(text_sin_espacios)
    return "La palabra es palindromo " if text_sin_espacios == texto_invertido else "La palabra no es palindromo"


texto = input("introduzca la palabra: >")
print(is_palindromo(texto))
