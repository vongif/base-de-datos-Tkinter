from tkinter import Tk
import vista


class Controlador:
    def __init__(self, aplicacion):
        self.aplicacion_controlador = aplicacion
        self.objeto_uno = vista.Ventana(self.aplicacion_controlador)


if __name__ == "__main__":
    aplicacion = Tk()
    aplication = Controlador(aplicacion)

    aplication.objeto_uno.actualizar()
aplicacion.mainloop()
