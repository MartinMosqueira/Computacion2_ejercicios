#! /usr/bin/python
import csv

with open('archivo.csv') as archivo:
    leerArchivo = csv.reader(archivo, delimiter=',', quotechar=',', 
                            quoting=csv.QUOTE_MINIMAL)

    for datoArchivo in leerArchivo:
        if datoArchivo[4] > 1200:
            print(datoArchivo[1])
