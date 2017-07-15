import paramiko
import threading
import os.path
import subprocess
import time
import sys
import re


#Checking IP address file and content validity
def ip_is_valid():
    check = False
    global ip_list
    
    while True:
        #Prompting user for input
        print "\n# # # # # # # # # # # # # # # # # # # # # # # # # # # #\n"
        ip_file = raw_input("# Enter IP file name and extension: ")
        print "\n# # # # # # # # # # # # # # # # # # # # # # # # # # # #"

    ############# Application #2 - Part #2 #############
    
    #Checking IP reachability
    print "\n* Checking IP reachability. Please wait...\n"
    
    check2 = False
    
    while True:
        for ip in ip_list:
            ping_reply = subprocess.call(['ping', '-c', '2', '-w', '2', '-q', '-n', ip])
            
            if ping_reply == 0:
                check2 = True
                continue
            
            elif ping_reply == 2:
                print "\n* No response from device %s." % ip
                check2 = False
                break
            
            else:
                print "\n* Ping to the following device has FAILED:", ip
                check2 = False
                break
            
        #Evaluating the 'check' flag 
        if check2 == False:
            print "* Please re-check IP address list or device.\n"
            ip_is_valid()
        
        elif check2 == True:
            print '\n* All devices are reachable. Waiting for username/password file...\n'
            break
