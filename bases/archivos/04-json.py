import json
from pathlib import Path

# escribir json
productos = [
    {"id": 1, "name": "laptop", "price": 1000},
    {"id": 2, "name": "mouse", "price": 20},
    {"id": 3, "name": "monitor", "price": 500}
]

data = json.dumps(productos)
Path("archivos/productos.json").write_text(data)


# leer json
data = Path("archivos/productos.json").read_text(encoding="utf-8")
productos = json.loads(data)
print(productos)
for producto in productos:
    print(producto["name"], producto["price"])


# modificar json
productos[0]["name"] = "micro"
Path("archivos/productos.json").write_text(json.dumps(productos))
