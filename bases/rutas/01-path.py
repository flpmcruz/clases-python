from pathlib import Path

# Crear un objeto Path
# Path(r"C:\Users\Usuario\Desktop\prueba.txt")  # Windows
# Path("/home/usuario/prueba.txt")  # Linux
# Path()  # Directorio actual
# Path.home()  # Directorio home
# Path("one/__init__.py")  # Directorio actual, ruta relativa

path = Path("hola-mundo/mi-archivo.txt")
path.is_file()  # True
path.is_dir()  # False
path.exists()  # True

print(
    path.name,  # mi-archivo.txt
    path.stem,  # mi-archivo
    path.suffix,  # .txt
    path.parent,  # hola-mundo
    path.absolute(),  # /home/usuario/hola-mundo/mi-archivo.txt
)  # mi-archivo.txt

p = path.with_name("mi-archivo2.txt")  # Cambiar nombre
p = path.with_suffix(".py")  # Cambiar extensión
p = path.with_stem("mi-archivo2")  # Cambiar nombre sin extensión
