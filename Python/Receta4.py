#Receta 4: Obtener una Cantidad Arbitraria de Elementos Mínimos y Máximos

import heapq

numeros = [7, 9, 1, 3, 5, 8, 7, 6, 2, 3, 1, 0, -8, -9, 5, -2]

print(heapq.nsmallest(3,numeros))

print(heapq.nlargest(3,numeros))
print()

productos = [
    { 'nombre': 'Mouse', 'precio': 35 },
    { 'nombre': 'Teclado', 'precio': 59 },
    { 'nombre': 'Monitor', 'precio': 279 },
    { 'nombre': 'Parlantes', 'precio': 120 },
    { 'nombre': 'Smartphone', 'precio': 455 }
]

mas_barato = heapq.nsmallest(2,productos,key=lambda p:['precio'])
resultado = 'El Producto mas Barato es: {0}'
print (resultado.format(mas_barato))

print()

resultado = 'El Producto mas Caro es: {0}'
mas_caro = heapq.nlargest(2,productos,key=lambda p: p['precio'])
print(resultado.format(mas_caro))
