#! /usr/bin/python
import argparse
import signal
import os
from sys import stdin
    
analizador = argparse.ArgumentParser()
analizador.add_argument('-f', help='archivo')
argumento = analizador.parse_args()

pid1=os.fork()
def recivir(signum,stack):
    if pid1 == 0:
        if argumento.f:
            Datos = stdin.read()
            archivo = open(argumento.f, 'w')
            archivo.write(Datos)
            archivo.close()
            exit()

pid2=os.fork()
def recivir1(signum,stack):
    if pid2 == 0:
        if argumento.f:
            archivo = open(argumento.f,'r')
            mayuscula = archivo.read().upper()
            archivo.close()
            archivo = open(argumento.f, 'w')
            archivo.write(mayuscula)
            archivo.close()
            exit()

def recivir3():
    if argumento.f:
        archivo=open(argumento.f, 'r')
        leer= archivo.read()
        print(leer)


signal.signal(signal.SIGUSR1,recivir)
signal.signal(signal.SIGUSR2,recivir1)

os.kill(os.getpid(),signal.SIGUSR1)
os.kill(os.getpid(),signal.SIGUSR2)
recivir3()
