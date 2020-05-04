from multiprocessing import Process, Pipe
import os
import argparse

analizador = argparse.ArgumentParser()
analizador.add_argument("-f", help="archivo")
argumento = analizador.parse_args() 

archivo=os.open(argumento.f, os.O_RDWR )

def proceso1 (argumento):    
    lectura = os.read(archivo,100).upper()
    invertir=lectura[::-1]
    argumento.send(invertir)
    argumento.close()

padre, hijo=Pipe()

p = Process ( target = proceso1 , args = (hijo,))

p . start ()
print(padre.recv())
p . join ()
