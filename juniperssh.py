from pprint import pprint
from jnpr.junos import Device
dev = Device(host='192.168.2.101', user='juniper', password='juniper123')
dev.open()
pprint(dev.facts)
dev.close()

