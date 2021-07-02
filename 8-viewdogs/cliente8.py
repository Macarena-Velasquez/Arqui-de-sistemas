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
                consulta = f"SELECT mascota.nombre, mascota.edad, mascota.raza, mascota.descripcion, usuario.nombre, usuario.apellido, usuario.contacto, usuario.email, usuario.region FROM mascota, usuario, usuariomascota WHERE mascota.idmascota = usuariomascota.idmascota AND usuario.idusuario = usuariomascota.idusuario;"
                respuesta = consultar(consulta)
                #print(respuesta)
                for i in respuesta:
                    nombreM = i[0]
                    edad = i[1]
                    raza = i[2]
                    desc = i[3]
                    nombreU = i[4]
                    apellido = i[5]
                    contacto = i[6]
                    email = i[7]
                    region = i[8]
                    print("Nombre mascota: ",nombreM,"\nEdad (meses): ",edad,"\nRaza: ",raza,"\nDescripcion: ",desc,"\nNombre dueñx: ",nombreU," ",apellido,"\nContacto: ",contacto,"\nEmail: ",email,"\nRegion: ",region)
                    print("-----------------------------")
                temp = llenado(len('viewd'))
                mensaje = temp + 'viewd'
                socket.send(bytes(mensaje,'utf-8'))
                recibido = socket.recv(4096)
                print(recibido[10:])
                print("fin cliente")

        print("ha cerrado terminal")

enviar()
socket.close()
