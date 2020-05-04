import argparse
import os

analizador = argparse.ArgumentParser(
    description='Calcular la potencia de multiples hijos.')
analizador.add_argument("-c", help="Cantidad de hijos.", type=int)
analizador.add_argument(
    "-v", help="modo verboso.", action='store_true', default=False)
argumento = analizador.parse_args()

for i in range(argumento.c):
    pid = os.fork()
    if pid == 0:
        exponente = int(input("ingrese el exponente: "))
        potencia = 2**exponente
        print("PID hijo: '%d' potencia: '%d'" % (os.getpid(), potencia))
        exit(0)

    else:
        os.wait()
print('PID padre:', os.getpid())

#-agregar modo verboso