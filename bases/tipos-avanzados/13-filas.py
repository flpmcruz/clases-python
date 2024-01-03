from collections import deque

fila = deque([1, 2, 3, 4, 5])

fila.append(6)
fila.append(7)

print(fila)

fila.popleft()

print(fila)

if not fila:
    print("La fila esta vacia")
