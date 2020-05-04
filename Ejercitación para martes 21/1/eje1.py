import signal
import os
import time

class Signal():
    def __init__(self):
        self.tiempo=1
        self.suma=0
        self.pausa=False

    def secuencia(self,tiempo):
        while True:
            self.suma = self.suma + 1
            print(self.suma)
            time.sleep(tiempo)
    
    def SIGUSR(self,signum,stack):
        if signum == 10:
            self.tiempo = self.tiempo*2
            self.secuencia(self.tiempo)

        elif signum == 12:
            if self.pausa == True:
                self.tiempo=1
                self.secuencia(self.tiempo)
            self.pausa=True    
            signal.pause()

instancia=Signal()

def recivir(signum,stack):
    instancia.SIGUSR(signum,stack)

signal.signal(signal.SIGUSR1,recivir)
signal.signal(signal.SIGUSR2,recivir)

print('mi PID es: ',os.getpid())
signal.pause()
