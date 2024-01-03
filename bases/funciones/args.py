def sumar(*args):  # el * indica que se recibiran varios argumentos y se guardaran en una tupla
    total = 0
    for valor in args:
        total += valor
    return total


print(sumar(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
