#Phayton 3 - Receta 6: Mapear a una Llave Múltiples Valores En Un Diccionario

from collections import defaultdict

diccionario_1 = {
    'a': [7, 9, 3],
    'b': [],
    'c': [9, 5, 3]
}

diccionario_2 = {
    'a': {7, 9, 3},
    'b': {},
    'c': {9, 5, 3}
}

diccionario_3 = defaultdict(list)

diccionario_3['a'].append(7)
diccionario_3['a'].append(9)
diccionario_3['a'].append(3)
diccionario_3['c'].append(9)
diccionario_3['c'].append(5)
diccionario_3['c'].append(3)

print(type(diccionario_2['a']))