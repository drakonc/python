import sys
from libreria.host import obtener_info_equipo
from libreria.consola import Consola

ip = sys.argv[1]

print('.:INFORMACION DEL EQUIPO LOCAL:.')
obtener_info_equipo()

cmd = Consola(ip)

print()
print('.:PING HACIA UN EQUIPO ESPECIFICO:.')
cmd.ping()

print()
print('.:INFORMACION DE LOS PUERTOS ABIERTOS DEL EQUIPO LOCAL:.')
cmd.puertos()