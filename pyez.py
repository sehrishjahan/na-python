from jnpr.junos import Device
from getpass import getpass
import sys

hostname = '192.168.2.14'
username = 'juniper'
password = 'cisco1234'

# NETCONF session over SSH
dev = Device(host=hostname, user=username, passwd=password)

# Telnet connection
#dev = Device(host=hostname, user=username, passwd=password, mode='telnet', port='23', gather_facts=True)

# Serial console connection
#dev = Device(host=hostname, user=username, passwd=password, mode='serial', port='/dev/ttyUSB0', gather_facts=True)

try:
    dev.open()
except Exception as err:
    print (err)
    sys.exit(1)

print (dev.facts)
dev.close()