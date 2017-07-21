from pprint import pprint
from jnpr.junos import Device
dev = Device(host='192.168.2.14', user='juniper', password='cisco1234')
dev.open()
pprint(dev.facts)
dev.close()
