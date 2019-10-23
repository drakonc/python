print("Datos de la Primera Persona")

# Para cargar por teclado una cadena de caracteres utilizamos la funcion input
# las variables pueden tener muchas funciones aqui una la utilizamos para almacenar el valor introducido por el teclado
nombre1 = input("Ingrese Nombre del Producto: ")
precio1 = int(input("Ingrese un Precio: $"))
nombre2 = input("Ingrese Nombre del Producto: ")
precio2 = int(input("Ingrese un Precio: $"))

# Esta es Una Constante 
BONIFICACION = 20
"""OPERADORES ESTAS COMILLAS SON PARA PONER COMENTARIOS MAS LARGOS DE UNA LINEA"""
#PARA COMENTARIOS DE UNA LINEA UTILIZAMOS ESTE SIGNO #
#sumamos los dos precios y su resultado lo guardamos en una variable
precio_compra_total = precio1 + precio2 # operador aritmetico
#comprobamos si el precio1 es mayor o igual a precio2
comprar = precio1 >= precio2 # operador comparacion
logico = (precio1 < precio2 and precio1 == precio2) # operacion logica

cabecera ="resultado del producto {0}. y el producto. {1}.:"
# concatenamos las cadenas de texto de varias forma aqui una con la funcion format
print(cabecera.format(nombre1,nombre2))
print("El Precio del primer valor es mayor o igual a el precio del segundo valor:")
print(comprar)
# concatenar se puede hacer de esta manera con el signo + y en la variable la propiedad str
print("la suma de los productos es: $" + str(precio_compra_total))
print("precio1 < precio2 and precio1 == precio2")
print(logico)
"""VEMOS EL OPERADOR DE ASIGNACION AQUI ABAJO"""
precio_compra_total += BONIFICACION # operador de asignacion
print("al precio total le incrementamos su valor que tiene la constante: $" + str(precio_compra_total))