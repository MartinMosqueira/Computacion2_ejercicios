#! /usr/bin/python
from sys import stdin

listaDatos = stdin.read().split()
for dato in range(len(listaDatos)):
    print(listaDatos[dato][::-1])
