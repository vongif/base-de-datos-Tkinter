import datetime


class Sujeto:

    observadores = []

    def agregar(self, obj):
        self.observadores.append(obj)

    def quitar(self, obj):
        pass

    def notificar(self, *args):
        for observador in self.observadores:
            observador.update(args)


class Observador:
    def update(self):
        raise NotImplementedError("Delegación de actualización")


class ConcreteObserverA(Observador):
    def __init__(self, obj):
        self.observado_a = obj
        self.observado_a.agregar(self)

    def update(self, *args):
        print("Actualización dentro de Observador A", "--" * 50)
        print("Aquí están los parámetros: ", args)
        archivo = open("registro.txt", "a")

        x = datetime.datetime.now()

        archivo.write(
            "AVISO !!!!! ------------  para Observador A. Se realizo un Alta:   "
            + str(args)
            + "\n"
            + "\n"
            + str((x))
        )
        return args
