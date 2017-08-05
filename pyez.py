import jnpr.junos
from jnpr.junos.device import Device
if __name__ == '__main__':
     junos_hosts = ['192.168.2.14']
     for ip in junos_hosts:
             dev = Device(host=ip, user='juniper', password='cisco1234')
             dev.open()
             print dev.facts
             dev.close()

