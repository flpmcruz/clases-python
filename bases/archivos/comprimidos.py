from pathlib import Path
from zipfile import ZipFile

with ZipFile("archivos/comprimidos.zip", "w") as zip:
    for path in Path().rglob("*.*"):
        if str(path) != "archivos/comprimidos.zip":
            zip.write(path)


with ZipFile("archivos/comprimidos.zip") as zip:
    print(zip.namelist())
    info = zip.getinfo("archivos/comprimidos.zip")
    print(
        info.file_size,
        info.compress_size,
        info.compress_size / info.file_size
    )
    zip.extractall("archivos/descomprimidos")
