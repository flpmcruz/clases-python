
try:
    n1 = int(input("Ingrese un número: "))
except Exception as e:
    print(type(e))
else:
    print("No hubo errores")
finally:
    print("Fin del programa")


# else: se ejecuta cuando no se producen excepciones.
# finally: se ejecuta siempre, haya o no excepciones.
