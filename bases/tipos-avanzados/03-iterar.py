mascotas = ["perro", "gato", "pez", "conejo", "elefante", "hormiga"]

for mascota in mascotas:
    print(mascota)


for i, mascota in enumerate(mascotas):
    print(f"{i}. {mascota}")


for mascota in enumerate(mascotas):
    print(mascota)  # (0, "perro") (1, "gato") (2, "pez") ...
    print(mascota[0])  # 0 1 2 ...
    print(mascota[1])  # "perro" "gato" "pez" ...
