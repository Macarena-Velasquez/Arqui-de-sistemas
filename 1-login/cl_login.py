#!/usr/bin/env python3
import bcrypt
import socket
#import time
#import datetime
from conect import *
import threading

socket = socket.socket()
PORT = 9999
socket.connect(("127.0.0.1",PORT))

def login ():
        while True:
                
                mail = input("Ingrese su e-mail: ")
                password = input("Ingrese su contraseña: ")

                #datos = nombre + " " + apellido + " " + rut + " " + pswAux2 + " " + contacto + " " + region + " " + emai
                datos = mail + " " + password
                temp = llenado(len(datos+'login'))
                mensaje = temp + 'login' + datos
                socket.send(bytes(mensaje,'utf-8'))
        
                recibido = socket.recv(4096)
                print(recibido[10:])
login()
socket.close()