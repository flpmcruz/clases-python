from pathlib import Path
from time import ctime

archivo = Path("archivos/archivo-prueba.txt")

# archivo.exists() # True
# archivo.rename("archivos/archivo-renombre.txt")
# archivo.unlink() # Elimina el archivo

print(archivo.stat())  # Información del archivo
print("acceso", ctime(archivo.stat().st_ctime))  # Fecha de creación
print("modificación", ctime(archivo.stat().st_mtime))  # Fecha de modificación
print("tamano", archivo.stat().st_size)  # Tamaño en bytes
