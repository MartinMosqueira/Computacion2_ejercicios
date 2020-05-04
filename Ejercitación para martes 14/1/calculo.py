import argparse

analizador = argparse.ArgumentParser(description='Calculadora matematica.')
grupo = analizador.add_mutually_exclusive_group()
grupo.add_argument("-s", help="suma dos numeros.", type=int, nargs=2)
grupo.add_argument("-r", help="resta dos numeros.", type=int, nargs=2)
grupo.add_argument("-m", help="multiplica dos numeros.", type=int, nargs=2)
grupo.add_argument("-d", help="divide dos numeros.", type=int, nargs=2)
analizador.add_argument(
    "-t", help="tipo de nros [int|float|real]", choices=['int', 'float', 'real'])
argumento = analizador.parse_args()
if argumento.s:
    suma = argumento.s[0] + argumento.s[1]
    print(suma)
elif argumento.r:
    resta = argumento.r[0] - argumento.r[1]
    print(resta)
elif argumento.m:
    mult = argumento.m[0] * argumento.m[1]
    print(mult)
elif argumento.d:
    div = argumento.d[0] / argumento.d[1]
    print(div)
else:
    print("Ningún argumento.")

# -falta agregar type  value:
#   int
#   float
#   real