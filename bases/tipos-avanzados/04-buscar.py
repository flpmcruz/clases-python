mascotas = ["perro", "gato", "pez", "conejo", "elefante", "hormiga"]

# print(mascotas.index("pez"))  # 2
# si el elemento no existe, lanza un ValueError

if "pez" in mascotas:
    print(mascotas.index("pez"))  # 2


print(mascotas.count("pez"))  # 1
