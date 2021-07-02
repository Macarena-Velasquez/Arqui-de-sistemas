import socket
import time
import datetime
from conect import *
import threading
import bcrypt

socket = socket.socket()
PORT = 5000

socket.connect(("127.0.0.1",PORT))
#print("A")
rutAux = ""
pswAux = ""
def enviar ():
        #print("A")

        while True:

                # se debe estar con sesión iniciada de entes , luego mover esto al if de op 1
                #socket.send(bytes('00010getsvadddi','utf-8'))

                #ingreso de datos
                # nombre apellido rut email contraseña contacto region
                email = "admin@mail.com" # aqui pasas el atributo de mail
                print("Sus datos de usuario: ")
                consulta = f"SELECT nombre, apellido, rut, email, pass, contacto, region, tipodeusuario, idusuario FROM usuario WHERE email='{email}';"
                datosU = consultar(consulta)
                n = datosU[0][0]
                a = datosU[0][1]
                r = datosU[0][2]
                e = datosU[0][3]
                p = datosU[0][4]
                c = datosU[0][5]
                re = datosU[0][6]
                t = datosU[0][7]
                id = datosU[0][8]
                if t == True:
                    t = "Administrador"
                if t == False:
                    t = "Usuario normal"
                print("Nombre completo: ",n,a,"\nRut: ",r,"\nEmail: ",e,"\nContraseña: ",p,"\nContacto: ",c,"\nRegion: ",re,"\nTipo de cuenta: ",t,"\nID usuario: ",id)
                print("-----------------------------")
                print("Editar datos: ")
                nombre = input("Escribir nombre: ")
                apellido = input("Escribir apellido: ")
                rut = input("Escribir rut: ")
                contraseña = input("Escribir contraseña: ")
                contacto = input("Escribir numero telefonico:")
                region = input("Escribir region:")

                salt = bcrypt.gensalt()
                psw2 = contraseña.encode()
                pswAux = bcrypt.hashpw(psw2, salt)
                pswAux2 = pswAux.decode()



                #envio de datos
                datos = nombre + " " + apellido + " " + rut +  " " + pswAux2 + " " + contacto + " " + region + " " + email
                temp = llenado(len(datos+'editu'))
                mensaje = temp + 'editu' + datos
                socket.send(bytes(mensaje,'utf-8'))
                #print(mensaje)

                recibido = socket.recv(4096)
                recibido = socket.recv(4096)
                print(recibido[10:])
                #recibido = socket.recv(4096)
                print("fin cliente")


        print("ha cerrado terminal")

enviar()
socket.close()
