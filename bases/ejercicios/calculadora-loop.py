
num1 = ""
num2 = ""
operacion = ""

while True:
    if num1 == "":
        num1 = input("Ingrese el primer numero: ")
        if num1 == "salir":
            break
    operacion = input("Ingrese la operacion a realizar: ")
    if operacion == "salir":
        break
    num2 = input("Ingrese el segundo numero: ")
    if num2 == "salir":
        break
    if operacion == "sumar":
        print("El resultado es: ", int(num1) + int(num2))
        num1 = int(num1) + int(num2)
    elif operacion == "restar":
        print("El resultado es: ", int(num1) - int(num2))
        num1 = int(num1) - int(num2)
    elif operacion == "multiplicar":
        print("El resultado es: ", int(num1) * int(num2))
        num1 = int(num1) * int(num2)
    elif operacion == "dividir":
        print("El resultado es: ", int(num1) / int(num2))
        num1 = int(num1) / int(num2)
    else:
        print("Operacion no valida")
