import platform
import subprocess

def ping(host):
    """
    Realiza un ping a un servidor/host.
    :param host: Nombre o deireccion del host
    """

    parametro = '-n' if platform.system().lower() == 'windows' else '-c'
    comando = ['ping',parametro,'1',host]

    subprocess.call(comando)

ping('192.168.253.1')    
