import sys
import os
import platform
import subprocess

plat = platform.system()
scriptDir = sys.path[0]
devices = os.path.join(scriptDir, 'devices.txt')
hostsFile = open(devices, "r")
lines = hostsFile.readlines()

if plat == "Linux":
    for line in lines:
        line = line.strip( )
        ping = subprocess.Popen(
            ["ping", "-c", "1", "-l", "1", "-s", "1", "-W", "1", line],
            stdout = subprocess.PIPE,
            stderr = subprocess.PIPE
        )
        if ping:
                print(ip, "inactive")
            else:
                print(ip, "active")
        
        out, error = ping.communicate()
        print out
        print error

hostsFile.close()
