import argparse
import os

analizador = argparse.ArgumentParser(
    description='Calcular potencia con un proceso hijo.')
analizador.add_argument("-n", help="base.", type=int)
analizador.add_argument("-m", help="exponente.", type=int)
analizador.add_argument(
    "-v", help="modo verboso.", action='store_true', default=False)
argumento = analizador.parse_args()

pid = os.fork()

if pid == 0:
    potencia = argumento.n**argumento.m
    print(potencia)

if argumento.v == True:
    if pid == 0:
        print("modo verboso...")
        print("argumentos ingresados: [('-v', '%s'), \
        ('-n', '%d'), ('-m', '%d')]" % ('', argumento.n, argumento.m))
        print("PID hijo:", os.getpid())
        print("PID padre:", os.getppid())
        print('potencia:', argumento.n**argumento.m, 'creado por:', os.getpid())
