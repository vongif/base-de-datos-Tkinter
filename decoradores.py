import re
from peewee import *
from types import MethodType



# DECORADOR ALTA-----------------------------------------------------------------------------------------------------


class Decorador_alta(object):
    def __init__(self, func):
        self.func = func
        print(self.func)

    def __call__(self, *args, **kwargs):
        print("Alta de nuevo registro  --------------------------")
        print(*args)
        print(**kwargs)
        print(self.func)
        return self.func(*args, **kwargs)

    def __get__(self, instance, cls):
        return self if instance is None else MethodType(self, instance)



# DECORADOR ELIMINAR-----------------------------------------------------------------------------------------------------


class Decorador_eliminar(object):
    def __init__(self, func):
        self.func = func
        print(self.func)

    def __call__(self, *args, **kwargs):
        print("Eliminacion de registro  --------------------------")
        print(*args)
        print(**kwargs)
        print(self.func)
        return self.func(*args, **kwargs)

    def __get__(self, instance, cls):
        return self if instance is None else MethodType(self, instance)


# DECORADOR ACTUALIZAR-----------------------------------------------------------------------------------------------------


class Decorador_actualizar(object):
    def __init__(self, func):
        self.func = func
        print(self.func)

    def __call__(self, *args, **kwargs):
        print("Se actualizaron los registros  --------------------------")
        print(*args)
        print(**kwargs)
        print(self.func)
        return self.func(*args, **kwargs)

    def __get__(self, instance, cls):
        return self if instance is None else MethodType(self, instance)
