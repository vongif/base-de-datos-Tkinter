from tkinter import Tk
import vista
import observador


class Controlador:
    def __init__(self, aplicacion):
        self.aplicacion_controlador = aplicacion
        self.objeto_uno = vista.Ventana(self.aplicacion_controlador)
        self.el_observador = observador.ConcreteObserverA(self.objeto_uno.objeto_uno)


if __name__ == "__main__":
    aplicacion = Tk()
    aplication = Controlador(aplicacion)

    aplication.objeto_uno.actualizar()
aplicacion.mainloop()
