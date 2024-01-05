def division(n=0):
    if n == 0:
        raise ZeroDivisionError("No se puede dividir por cero")
    return 10 / n


try:
    division()
except ZeroDivisionError as e:
    print(e)  # Recibe el string que se le pasa al constructor de la excepción


def division2(n=0):
    if n == 0:
        raise ZeroDivisionError("No se puede dividir por cero", f"{n}")
    return 10 / n


try:
    division2()
except ZeroDivisionError as e:
    print(e)  # Recibe todos los argumentos que se le pasan al constructor de la excepción, en forma de tupla

# Las excepciones se pueden invocar manualmente con la palabra reservada raise.
# Son costosas en términos de rendimiento, por lo que se recomienda usarlas solo cuando sea necesario.
