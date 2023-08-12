import socket
import sys
import binascii
import observador
import decoradores


HOST, PORT = "localhost", 9999
data = " ".join(sys.argv[1:])
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# ################################################
mensaje = "Hello, World!"

sock.sendto(mensaje.encode("UTF-8"), (HOST, PORT))
received = sock.recvfrom(1024)


print("Recibi el alta del registro:  ")
print("seeeeee", observador.ConcreteObserverA.update)

archivo = open("registro_cliente.txt", "a")
archivo.write(str(object) + "\n" + "\n")

print("seeeeee", decoradores.decorador_alta)

print("Estoy conectado  " + "--------------------------------")


# ===== FIN ENVIO Y RECEPCIÓN DE DATOS =================
