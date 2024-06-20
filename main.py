import requests
import os
import raducord
import string
from raducord import Logger, Console, ColorUtils
import getpass
import cryptography
from cryptography.fernet import Fernet
import socket
import pyautogui
import fake_headers
from fake_headers import Headers
import tempmail
from validate_email_address import validate_email
import random
from tempmail import EMail
import time
import pystyle
import nmap
import threading
from pystyle import Write, Colors

def menu():
    os.system('cls')
    Write.Print("""
  ██████ ▓█████  ▄████▄   █    ██  ██▀███   ██▓▄▄▄█████▓▓██   ██▓
▒██    ▒ ▓█   ▀ ▒██▀ ▀█   ██  ▓██▒▓██ ▒ ██▒▓██▒▓  ██▒ ▓▒ ▒██  ██▒
░ ▓██▄   ▒███   ▒▓█    ▄ ▓██  ▒██░▓██ ░▄█ ▒▒██▒▒ ▓██░ ▒░  ▒██ ██░
  ▒   ██▒▒▓█  ▄ ▒▓▓▄ ▄██▒▓▓█  ░██░▒██▀▀█▄  ░██░░ ▓██▓ ░   ░ ▐██▓░
▒██████▒▒░▒████▒▒ ▓███▀ ░▒▒█████▓ ░██▓ ▒██▒░██░  ▒██▒ ░   ░ ██▒▓░
▒ ▒▓▒ ▒ ░░░ ▒░ ░░ ░▒ ▒  ░░▒▓▒ ▒ ▒ ░ ▒▓ ░▒▓░░▓    ▒ ░░      ██▒▒▒ 
░ ░▒  ░ ░ ░ ░  ░  ░  ▒   ░░▒░ ░ ░   ░▒ ░ ▒░ ▒ ░    ░     ▓██ ░▒░ 
░  ░  ░     ░   ░         ░░░ ░ ░   ░░   ░  ▒ ░  ░       ▒ ▒ ░░  
      ░     ░  ░░ ░         ░        ░      ░            ░ ░     
                ░                                        ░ ░     
""", Colors.black_to_white, interval=0.000)
    
    Write.Print(""" 
 01> Ciber Security Menu                          
 02> Email Menu                     
 03> SMS Menu                         
 04> Extra Menu                                      
""", Colors.blue_to_white, interval=0.000)
    




    opc = Write.Input('\nroot@w1s>', Colors.cyan_to_green)




    if opc == '3':
       Logger.failed('Error,option in dev,...')
       time.sleep(3)
    if opc == '4':
       Logger.failed('Error,option in dev,...')
       time.sleep(3)

    if opc == '2':
      ruta_script1 = "modules/email.py"

      with open(ruta_script1, 'r') as file:
          codigo_script1 = file.read()

      os.system('cls')
      exec(codigo_script1)











    if opc == '1':
      ruta_script2 = "modules/ciber_security.py"



      with open(ruta_script2, 'r') as file:
        codigo_script2 = file.read()

    os.system('cls')
    exec(codigo_script2)

    

menu()


  