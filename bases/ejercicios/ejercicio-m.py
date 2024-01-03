from pprint import pprint
string = 'Hola mando'


# def quitar_espacios3(cadena):
#     return cadena.replace(' ', '')


# def quitar_espacios2(cadena):
#     return ''.join(cadena.split())


def quitar_espacios(cadena):
    return [char for char in cadena if char != ' ']


def cuenta_caracteres(lista):
    chars_dict = {}
    for char in lista:
        if char in chars_dict:
            chars_dict[char] += 1
        else:
            chars_dict[char] = 1
    return chars_dict


def ordena(diccionario):
    return sorted(
        diccionario.items(),
        key=lambda key: key[1],
        reverse=True
    )


def caracteres_mas_frecuentes(cadena):
    maximo = cadena[0][1]
    dic = {}
    for i in cadena:
        if i[1] == maximo:
            dic[i[0]] = i[1]
        else:
            break
    return dic


sin_espacios = quitar_espacios(string)
contados = cuenta_caracteres(sin_espacios)
ordenados = ordena(contados)
mas_frecuentes = caracteres_mas_frecuentes(ordenados)

print(mas_frecuentes)
