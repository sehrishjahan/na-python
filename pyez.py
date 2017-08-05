import jnpr.junos
from jnpr.junos.device import Device
junos_host = '192.168.2.14'
dev = Device(host=junos_host, user='juniper', password='cisco1234')
dev.open()
print dev.facts
dev.close()

