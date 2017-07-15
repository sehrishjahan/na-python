import os

def ipcheck():
    status = os.system("ping -c 3 " + str(pop))
    if status == 0:
        print("System " + str(pop) + " is UP !")
    else:
        print("System " + str(pop) + " is DOWN !")


pop = input("Enter the ip address: ")
ipcheck()
