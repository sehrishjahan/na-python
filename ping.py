import os

def ping():
    response = os.system("ping -c 3 " + s)
    #check the response
    if response == 0:
        print("System " + s + " is UP !")
    else:
        print("System " + s + " is DOWN !")
        #Prompting user for ip address
s = raw_input('Enter the ip address: ')  
ping() #calling ping function
