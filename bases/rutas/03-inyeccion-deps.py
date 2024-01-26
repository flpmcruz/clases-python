from pathlib import Path

path = Path()

paths = [p for p in path.iterdir() if p.is_dir()]

dependencias = {
    "db": "base de datos",
    "api": "api rest",
    "graphql": "graphql",
}


def load(p):
    # print(str(p))
    paquete = __import__(str(p).replace('/', '.'))
    try:
        paquete.init(**dependencias)
    except:
        print("no tiene init")


list(map(load, paths))
