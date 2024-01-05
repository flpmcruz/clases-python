
class MiError(Exception):
    "Esta clase hereda de Exception"

    def __init__(self, mensaje, codigo):
        self.mensaje = mensaje
        self.codigo = codigo

    def __str__(self):
        return f"{self.mensaje} - codigo: {self.codigo}"


try:
    raise MiError("Este es mi mensaje de error", 404)
except MiError as e:
    print(e)
    print(e.mensaje, e.codigo)
