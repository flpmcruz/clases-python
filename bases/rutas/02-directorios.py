from pathlib import Path

path = Path("rutas")

# path.mkdir()  # Crear directorio
# path.rmdir()  # Eliminar directorio, tiene que estar vacío
# path.exists()  # True
# path.is_dir()  # True
# path.rename("directorio2")  # Renombrar directorio


print(path.iterdir())  # <generator object Path.iterdir at 0x7f9b1c0b6f90>

for p in path.iterdir():
    print(p)

archivos = [p for p in path.iterdir() if p.is_file()]
archivos2 = [p for p in path.glob("*.py") if p.is_file()]
archivos3 = [p for p in path.rglob("*.py") if p.is_file()]
print(archivos3)
