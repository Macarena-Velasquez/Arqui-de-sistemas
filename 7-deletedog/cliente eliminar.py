import socket
import time
import datetime
from conect import *
import threading

socket = socket.socket()
PORT = 9999

socket.connect(("127.0.0.1",PORT))
#print("A")
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
        #print("A")
    
        while True:

                #email
                email1 = "elipareja1998@gmail.com"

                # se debe estar con sesión iniciada de entes , luego mover esto al if de op 1
                #socket.send(bytes('00010getsvadddi','utf-8'))

                #ID USUARIO:
                consulta0= f"SELECT idusuario FROM usuario WHERE email='{email1}';"
                idusuario1 = consultar(consulta0)
                idusuario1 = limpiar(idusuario1)

                #RELACION USUARIO PERRO
                consulta1= f"SELECT idmascota FROM usuariomascota where idusuario = '{idusuario1}';"
                idmascota1 = consultar(consulta1)

                #PERROS DISPONIBLES
                print("Sus perros ingresados: ")
                for gg in idmascota1:
                        gg = limpiar(gg)
                        
                        a = consultar(f"SELECT nombre, edad, raza, descripcion, idmascota FROM mascota where idmascota = '{gg}';")
                        print(a)

                #ingreso de ide
                print("AVISO: En el arreglo del perro el ULTIMO NUMERO es el ID del animal")
                ide = input("Ingrese id de animal a eliminar: ")

                #envio de datos viejos
                datos = ide + " " + "jaja"
                temp = llenado(len(datos+'elimd'))
                mensaje = temp + 'elimd' + datos
                socket.send(bytes(mensaje,'utf-8'))
        
                recibido = socket.recv(4096)
                print(recibido[10:])
                print("fin cliente")
                

        print("ha cerrado terminal")
        
enviar()
socket.close()
        
