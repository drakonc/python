#Phayton 3 - Receta 7: Uso de las Estructuras de Datos deque

from collections import deque

letras = deque('ytho')

print(letras)

letras.appendleft('P')

print(letras)

letras.append('n')

print(letras)

print(letras.count('t'))

letras.popleft()

print(letras)

letras.pop()

print(letras)

letras.extend('n Es Genial')

print(letras)

letras.extendleft('P')

print(letras)