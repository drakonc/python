#Python 3 - Receta 210: Ejecutar un Thread en Modo Daemon

from threading import Thread
import time

def temporizador(n):
    while n > 0:
        print(n)
        n-=1
        time.sleep(2)

t = Thread(target=temporizador,args=(10, ), daemon=True)
t.start()

while t.isAlive():
    pass

print('FIn de __main__')