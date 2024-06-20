import tempmail
from tempmail import EMail
import requests
import pystyle
from pystyle import Write, Colors
import raducord
from raducord import Logger, Console
import time
from validate_email_address import validate_email
import os

os.system('cls')

Write.Print("""
 ______     __    __     ______     __     __            __    __     ______     __   __     __  __    
/\  ___\   /\ "-./  \   /\  __ \   /\ \   /\ \          /\ "-./  \   /\  ___\   /\ "-.\ \   /\ \/\ \   
\ \  __\   \ \ \-./\ \  \ \  __ \  \ \ \  \ \ \____     \ \ \-./\ \  \ \  __\   \ \ \-.  \  \ \ \_\ \  
 \ \_____\  \ \_\ \ \_\  \ \_\ \_\  \ \_\  \ \_____\     \ \_\ \ \_\  \ \_____\  \ \_\\"\_\  \ \_____\ 
  \/_____/   \/_/  \/_/   \/_/\/_/   \/_/   \/_____/      \/_/  \/_/   \/_____/   \/_/ \/_/   \/_____/ 
                                                                                                       
""", Colors.blue_to_cyan, interval=0.00)

Write.Print(""" 
1 > Email Temp
2 > Email Leaks
3 > Email Bomber(Only Paid Version)
4 > Email Verify
5 > Check Temporaly Mail
""", Colors.black_to_white, interval=0.00000001)

opc2 = Write.Input('root@email>', Colors.black_to_white)



if opc2 == '5':
    def check_temporary_email(email):
        temporary_domains = ["tempmail", "guerrillamail", "mailinator", "10minutemail", "dispostable",
                        "tempinbox", "tempmailaddress", "tempmailer", "tempmailer", "guerrillamailblock",
                        "mailinator2", "10minutemail", "throwawayemailaddress"]

        domain = email.split('@')[-1]

        for temp_domain in temporary_domains:
            if temp_domain in domain:
                print(f"Warning! The email '{email}' uses a domain known to provide temporary email services.")
                return True
        
        print(f"The email '{email}' does not appear to be temporary.")
        return False

    email_address = input("Enter the email address to check: ")
    check_temporary_email(email_address)




if opc2 == '4':
    def check_email_exists(email):
        is_valid = validate_email(email)

        if is_valid:
            print(f"The email '{email}' is valid.")
        else:
            print(f"The email '{email}' is not valid.")

    email_to_check = input("Enter the email address to check: ")
    check_email_exists(email_to_check)




if opc2 == '3':
    Logger.failed('Error,Only Customers,...')
    time.sleep(2.5)



if opc2 == '1':
    Logger.info('Wait,Generating Mail,...')
    time.sleep(1.2)
    email = EMail()
    Logger.success(f'Sucess,email generated,{email.address}')
    time.sleep(0.80)
    Logger.warning('Waiting,Waiting for message,240 seconds')
    msg = email.wait_for_message(timeout=240)
    print(msg.body)

if opc2 == '2':
    def search_email_leaks(email):
        url = f"https://haveibeenpwned.com/api/v3/breachedaccount/{email}"

        response = requests.get(url)

        if response.status_code == 200:
            print(f"The email '{email}' has been found in the following data breaches:")
            for breach in response.json():
                print(f"- {breach['Name']}")
        elif response.status_code == 404:
            print(f"No breaches found for the email '{email}'.")
        else:
            print(f"Error searching for breaches for email '{email}': {response.status_code}")

email_to_check = input("Enter the email address to check for leaks: ")
search_email_leaks(email_to_check)














