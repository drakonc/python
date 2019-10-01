#Python 3 - Receta 211: Crear una Clase para Controlar la Finalización de un Thread

from threading import Thread
import time

class ContadorTarea:

    def __init__(self):
        self._ejecutandose = True
    
    def finalizar(self):
        self._ejecutandose = False

    def ejecutar(self, n):
        while self._ejecutandose and n > 0:
            print('Valor Actual de n: {}'.format(n))
            n -= 1
            time.sleep(2)
    

c = ContadorTarea()
t = Thread(target=c.ejecutar, args=(10,))
t.start()

c.finalizar()
print('FIn de __main__')
t.join()