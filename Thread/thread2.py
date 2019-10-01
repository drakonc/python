#Python 3 - Receta 209: Usar el Método join para Esperar Hasta Finalizar un Thread

from threading import Thread
import time

def temporizador(n):
    while n > 0:
        print(n)
        n-=1
        time.sleep(2)

t = Thread(target=temporizador,args=(10, ))
t.start()
t.join()#Ejecutar un Hilo y hasta ue no finalice no se continua con la ejecucion del resto de codigo


print('FIn de __main__')