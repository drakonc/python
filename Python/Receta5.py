#Phayton 3 - Receta 5: Diccionario en Orden a Través de la clase OrderedDict

from collections import OrderedDict

productos = {7:'Mouse', 5:'Teclado', 6:'Parlantes', 1:'Monitor', 2:'Control'}

print(OrderedDict(sorted(productos.items(),key=lambda p : p[0])))

print(OrderedDict(sorted(productos.items(),key=lambda p : p[1])))

print(OrderedDict(sorted(productos.items(),key=lambda p : len(p[1]))))