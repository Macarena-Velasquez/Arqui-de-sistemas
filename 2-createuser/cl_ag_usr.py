#!/usr/bin/env python3
import bcrypt
import socket
from conect import *
import threading

socket = socket.socket()
PORT = 9999
socket.connect(("127.0.0.1",PORT))
pswAux = ""

def enviar ():
        while True:
                #nombre, apellido, rut, pass, contacto, region, email
                print("Para crear su cuenta de usuario, ingrese sus datos a continuación.")
                nombre = input("Nombre: ")
                apellido = input("Apellido: ")
                rut = input("RUT: ")
                psw = input("Contraseña: ")
                contacto = input("Numero de contacto: ")
                region = input("Región de residencia: ")
                email = input("E-mail: ")
                #--------------HASH----------------
                salt = bcrypt.gensalt()
                psw2 = psw.encode()
                pswAux = bcrypt.hashpw(psw2, salt)
                pswAux2 = pswAux.decode()
                #----------------------------------
                #envio de datos
                datos = nombre + " " + apellido + " " + rut + " " + pswAux2 + " " + contacto + " " + region + " " + email
                temp = llenado(len(datos+'agusr'))
                mensaje = temp + 'agusr' + datos
                socket.send(bytes(mensaje,'utf-8'))
        
                recibido = socket.recv(4096)
                print(recibido[10:])
enviar()
socket.close()