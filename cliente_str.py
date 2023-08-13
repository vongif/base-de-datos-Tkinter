import socket
import sys
import binascii
import observador
import decoradores
import datetime


HOST, PORT = "localhost", 9999
data = " ".join(sys.argv[1:])
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# ################################################
mensaje = "Hello, World!"

sock.sendto(mensaje.encode("UTF-8"), (HOST, PORT))
received = sock.recvfrom(1024)


class Cliente_servidor:
    def __init__(self, obj):
        self.observado_a = obj
        self.observado_a.agregar(self)

    def cliente(self, *args):
        print("Recibi el alta del registro:  ")
        print("seeeeee", observador.ConcreteObserverA)
        archivo = open("registro_cliente.txt", "a")
        x = datetime.datetime.now()
        archivo.write(
            "AVISO !!!!! ------------  para Observador A. Se realizo un Alta:   "
            + str(args)
            + "\n"
            + "\n"
            + str((x))
        )
        return args


print("seeeeee", Cliente_servidor.cliente(str(set.update)))
# archivo = open("registro_cliente.txt", "a")
# archivo.write(str(object) + "\n" + "\n")
print("seeeeee", decoradores.decorador_alta)




# ===== FIN ENVIO Y RECEPCIÓN DE DATOS =================
