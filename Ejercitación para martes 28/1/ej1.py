import os
import argparse

analizador = argparse.ArgumentParser()
analizador.add_argument("-f", help="archivo")
argumento = analizador.parse_args()    

r,w=os.pipe()

pid = os.fork()

archivo=os.open(argumento.f, os.O_RDWR )

if pid == 0:
    os.close(r)
    lectura = os.read(archivo,100).upper()
    invertir=lectura[::-1]
    os.write(w,invertir)
    exit(0)

else:
    os.close(w)
    leer=os.read(r,100)
    print(leer)
