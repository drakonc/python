import sys
import platform
import subprocess
from subprocess import Popen,PIPE
from socket import AF_INET,SOCK_STREAM,socket

class Consola:

    def __init__(self,ip):
        self.ip = ip
        self.parametro = '-n' if platform.system().lower() == 'windows' else '-c'
        self.puerto = 1
        self.conectado = None
        self.s = None
        self.line = None


    def ping(self):
        self.comando = ['ping',self.parametro,'4',self.ip]
        subprocess.call(self.comando)

    def tracert(self):
        self.s = Popen(['traceroute', self.ip ], stdout=PIPE)
        while True:
            self.line = self.s.stdout.readline()
            if not self.line:
                break
    
    def puertos(self):
        while self.puerto <= 65535:
            try:
                try:
                    self.s = socket(AF_INET,SOCK_STREAM,0)
                except:
                    print('Error No se Puede Abrir Este Socket')
                    break
                self.s.connect(('localhost',self.puerto ))
                self.conectado = True
            except Exception:
                self.conectado = False
            finally:
                if self.conectado and self.puerto != self.s.getsockname()[1]:
                    print('El Puerto '+ str(self.puerto) +' está activo.')
                self.puerto  += 1
                self.s.close()
