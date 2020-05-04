#! /usr/bin/python
import os.path

origen = raw_input('ingrese archivo origen: ')
destino = raw_input('ingrese archivo destino: ')

if os.path.exists(origen) and os.path.exists(destino):
    archivoOrigen = open(origen, 'r')
    contenido_archivoOrigen = archivoOrigen.read()
    archivoDestino = open(destino, 'a')
    archivoDestino.write(contenido_archivoOrigen + os.linesep)
    archivoOrigen.close()
    archivoDestino.close()
else:
    print('el archivo origen o destino no existe...')
    