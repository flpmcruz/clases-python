from abc import ABC, abstractmethod

# Clase abstracta, esta es la forma de definir una clase abstracta en Python


class Model(ABC):
    # Este decorador es el que hace que el método sea abstracto
    @property
    @abstractmethod
    def tabla(self):
        pass

    @abstractmethod
    def guardar(self):
        pass  # No hace nada, obliga a que las clases que hereden de esta clase implementen este método

    @classmethod
    def buscar_por_id(cls, id):
        print(f'Buscando en la tabla {cls.tabla} el id {id}')


class Usuario(Model):
    tabla = 'usuarios'

    def guardar(self):
        print(f'Guardando en la tabla {self.tabla}')


usuario = Usuario()
usuario.guardar()
Usuario.buscar_por_id(1)
