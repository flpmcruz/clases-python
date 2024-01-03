# las pilas se implementan con listas con una forma logicamente correcta

pila = [3, 4, 5]
pila.append(6)
pila.append(7)


print(pila)

# sacar el ultimo elemento de la pila
n = pila.pop()
print(n)
print(pila)


# acceder al ultimo elemento de la pila
print(pila[-1])

# si la pila esta vacia
if not pila:
    print("La pila esta vacia")
