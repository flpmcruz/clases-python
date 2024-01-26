texto = input("Ingrese un texto: ").lower()

letra1 = input("Ingrese una letra: ").lower()
letra2 = input("Ingrese otra letra: ").lower()
letra3 = input("Ingrese otra letra: ").lower()

print(f"La letra {letra1} aparece {texto.count(letra1)} veces")
print(f"La letra {letra2} aparece {texto.count(letra2)} veces")
print(f"La letra {letra3} aparece {texto.count(letra3)} veces")

print(f"Hay {len(texto.split())} palabras en el texto")
print(f"La primera letra del texto es {texto[0]}")
print(f"La ultima letra del texto es {texto[-1]}")


print(texto.split().reverse())


print(f"La palabra python aparece {texto.count('python')} veces")
