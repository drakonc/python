#Receta 3: Obtener los elementos mas frecuentes en una lista

from collections import Counter

numeros = [4, 7, 9, 9, 4, 2, 5, 7, 3, 3, 5, 4, 9, 9]

contador = Counter(numeros)

print(contador.most_common(3))

palabra = 'Python es un lenguaje de programación'

print(Counter(palabra).most_common(2))