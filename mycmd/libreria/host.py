import sys
import socket

def obtener_info_equipo():
	nombre_equipo = socket.gethostname()
	direccion_equipo = socket.gethostbyname(nombre_equipo)
	print ("el nombre del equipo Local Es: %s" % nombre_equipo)
	print ("La IP es: %s" % direccion_equipo)