import csv
import os

# escritura
with open("archivos/archivo.csv", "w") as archivo:
    writer = csv.writer(archivo, lineterminator='\n')
    writer.writerow(["nombre", "apellido", "edad"])
    writer.writerow(["Juan", "Perez", 30])
    writer.writerow(["Maria", "Gomez", 25])
    writer.writerow(["Carlos", "Gutierrez", 40])

# leer
# with open("archivos/archivo.csv", "r") as archivo:
#     reader = csv.reader(archivo)
#     print(reader)
#     archivo.seek(0)
#     for linea in reader:
#         print(linea)

# actualizar CSV

with open("archivos/archivo.csv") as r, open("archivos/archivo_tmp.csv", "w") as w:
    reader = csv.reader(r)
    writer = csv.writer(w, lineterminator='\n')
    writer.writerow(["nombre", "apellido", "edad"])
    for linea in reader:
        if linea[0] == "Juan":  # cada linea es una lista de strings, que representan cada columna
            writer.writerow(["Pedro E", "Perez", 31])
        else:
            writer.writerow(linea)

os.remove("archivos/archivo.csv")
os.rename("archivos/archivo_tmp.csv", "archivos/archivo.csv")
