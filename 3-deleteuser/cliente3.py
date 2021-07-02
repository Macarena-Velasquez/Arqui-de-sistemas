import socket
import time
import datetime
from conect import *
import threading

socket = socket.socket()
PORT = 5000

socket.connect(("127.0.0.1",PORT))
rutAux = ""
def limpiar(var):
        var = str(var)
        var = var.replace("[","")
        var = var.replace("(","")
        var = var.replace("]","")
        var = var.replace(")","")
        var = var.replace(",","")
        return var
def enviar ():
        while True:
                #ingreso de datos
                # email loggeado y email para borrar
                email = "admin@mail.com"
                # seleccionar tipo de usuario del usuario loggeado
                consulta0 = f"SELECT tipodeusuario FROM usuario where email='{email}';"
                tipousuario = consultar(consulta0)
                tipousuario = limpiar(tipousuario)
                if tipousuario != "True":
                    print("No tiene permiso para realizar esta accion")
                    email_borrar = "-"
                if tipousuario == "True":
                    email_borrar = input("Escribir email para borrar su usuario: ")
                #envio de datos
                datos = email + " " + email_borrar
                temp = llenado(len(datos+'deltu'))
                mensaje = temp + 'deltu' + datos
                socket.send(bytes(mensaje,'utf-8'))


                recibido = socket.recv(4096)
                print(recibido[10:])
                print("fin cliente")


        print("ha cerrado terminal")

enviar()
socket.close()
