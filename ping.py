import platform
import subprocess
import socket
import sys

print('\n')
print('.:SERVER PING:.')
print('\n')

def ping(host,it):
    """
    Realiza un ping a un servidor/host.
    :param host: Nombre o deireccion del host
    :param it: Numero de Iteraciones
    """

    parametro = '-n' if platform.system().lower() == 'windows' else '-c'
    comando = ['ping',parametro,it,host]

    subprocess.call(comando)

def obtener_info_equipo():
	nombre_equipo = socket.gethostname()
	direccion_equipo = socket.gethostbyname(nombre_equipo)
	print ("el nombre del equipo es: %s" % nombre_equipo)
	print ("La IP es: %s" % direccion_equipo)

host = sys.argv[1]
it = sys.argv[2]

obtener_info_equipo()

ping(host,it)    
