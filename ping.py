import os

def ipcheck():
    status = os.system("ping -c 3 " + s)
            print "\n# # # # # # # # # # # # # # # # # # # # # # # # # # # #\n"

    if status == 0:
        print("System " + s + " is UP !")
    else:
        print("System " + s + " is DOWN !")


s = raw_input('Enter the ip address: ')
ipcheck()
