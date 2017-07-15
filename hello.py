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
   
        print "\n# # # # # # # # # # # # # # # # # # # # # # # # # # # #\n"
        ip_file = raw_input("# Enter IP file name and extension: ")
        print "\n# # # # # # # # # # # # # # # # # # # # # # # # # # # #"
        print (raw_input)
