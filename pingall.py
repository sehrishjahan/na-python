import sys
import os
import platform
import subprocess

plat = platform.system()
scriptDir = sys.path[0]
devices = os.path.join(scriptDir, 'devices.py')
hostsFile = open(devices, "r")
lines = hostsFile.readlines()

if plat == "Linux":
    for line in lines:
        line = line.strip( )
        ping = os.system("ping -c 1 ", line)

       
        out, error = ping.communicate()
        print out
        print error

hostsFile.close()
