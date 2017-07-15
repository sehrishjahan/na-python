from netmiko import ConnectHandler
 from pyIOSXR import IOSXR

platform = 'cisco_ios'
host = '192.168.2.110'
username = 'csrv'
password = 'cisco1234'
#device = ConnectHandler(device_type=platform, ip=host, username=username, password=password)

device = IOSXR(hostname='host', username='csrv', password='cisco1234', port=22, lock=False)
device.open()
