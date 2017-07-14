from pprint import pprint
from jnpr.junos import Device
dev = Device(host='192.168.3.99', user='andrew', password='Andrew')
dev.open()
pprint(dev.facts)
dev.close()