import os

def ping():
    response = os.system("ping -c 3 " + s)

    if response == 0:
        print("System " + s + " is UP !")
    else:
        print("System " + s + " is DOWN !")


s = raw_input('Enter the ip address: ')         #Prompting user for ip address

ping()
