
primer = set([1, 2, 3, 4, 5])
segundo = {1, 1, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

print(primer)
print(segundo)

# Operaciones con conjuntos
primer.add(11)
primer.remove(1)

union = primer | segundo  # une los conjuntos
print(union)

interseccion = primer & segundo  # elementos en comun
print(interseccion)

# elementos que estan en el primer conjunto pero no en el segundo
diferencia = primer - segundo
print(diferencia)

# elementos que estan en un conjunto o en otro pero no en ambos
diferenciaSimetrica = primer ^ segundo

if 1 in primer:
    print("Si esta en el conjunto")
