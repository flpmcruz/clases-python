

def devolver_distintos(*args):
    suma = 0
    minimo = min(args)
    maximo = max(args)
    intermedio = 0

    for n in args:
        suma = suma + n
        if n not in (minimo, maximo):
            intermedio = n

    print(minimo, maximo, intermedio)

    if suma > 15:
        return maximo
    elif suma < 10:
        return minimo
    else:
        return intermedio


print(devolver_distintos(3, 6, 9))
