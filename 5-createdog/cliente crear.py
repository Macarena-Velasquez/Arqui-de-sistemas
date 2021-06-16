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

def enviar ():
        #print("A")
    
        while True:

                # se debe estar con sesión iniciada de entes , luego mover esto al if de op 1
                #socket.send(bytes('00010getsvadddi','utf-8'))

                print("perros disponibles")

                a = consultar("SELECT * FROM mascota;")
                print(a)

                #ingreso de datos
                nombre = input("Escribir nombre: ")
                edad = input("Escribir edad en meses: ")
                raza = input("Escribir raza o callejero: ")
                descripcion = input("Escribir descripción corta: ")

                #envio de datos
                datos = nombre + " " + edad + " " + raza + " " + descripcion
                temp = llenado(len(datos+'addco'))
                mensaje = temp + 'addco' + datos
                socket.send(bytes(mensaje,'utf-8'))
                #print(mensaje)

        
                recibido = socket.recv(4096)
                print(recibido[10:])
                print("fin cliente")
                

        print("ha cerrado terminal")
        
enviar()
socket.close()
        
