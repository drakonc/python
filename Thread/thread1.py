#Python 3 - Receta 208: Iniciar un Thread con el Método start de la Clase Thread

from threading import Thread
import time

def temporizador(n):
    while n > 0:
        print(n)
        n-=1
        time.sleep(2)

t = Thread(target=temporizador,args=(10, ))
t.start()

print('FIn de __main__')