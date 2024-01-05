try:
    n1 = int(input("Ingrese un número: "))
    unerrir
except ValueError:
    print("No ingresaste un número")
except NameError:
    print("No existe unerrir")
except Exception as e:
    print(type(e))

# Existen muchos tipos de excepciones, pero las más comunes son:
# ValueError: cuando el tipo de dato es correcto, pero el valor no.
# TypeError: cuando el tipo de dato es incorrecto.
# NameError: cuando se intenta usar una variable que no existe.
# ZeroDivisionError: cuando se intenta dividir por cero.
# IndexError: cuando se intenta acceder a un índice que no existe.
# KeyError: cuando se intenta acceder a una clave que no existe.
# AttributeError: cuando se intenta acceder a un atributo que no existe.
# FileNotFoundError: cuando se intenta acceder a un archivo que no existe.
# OSError: cuando se intenta acceder a un archivo que no existe.
# ImportError: cuando se intenta importar un módulo que no existe.
# KeyboardInterrupt: cuando se interrumpe la ejecución del programa.
# EOFError: cuando se llega al final del archivo.
# Exception: cuando se produce cualquier otro tipo de excepción.
