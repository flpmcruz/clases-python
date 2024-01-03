n1 = input("Digite el primer numero: ")
n2 = input("Digite el segundo numero: ")

suma = int(n1) + int(n2)
resta = int(n1) - int(n2)
multiplicacion = int(n1) * int(n2)
division = int(n1) / int(n2)

mensaje = f"""
Para los numeros {n1} y {n2}:
el resultado de la suma es {suma}
el resultado de la resta es {resta}
el resultado de la multiplicacion es {multiplicacion}
el resultado de la division es {division}
"""
print(mensaje)
