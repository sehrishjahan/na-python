
from netmiko import ConnectHandler
import getpass

csrv = {    
    'device_type': 'cisco_ios',
    'ip': '192.168.2.11',
    'username': 'csrv',
    'password': 'telnet',
}

csrv2 = { 
    'device_type': 'cisco_ios',
    'ip': '192.168.2.12',
    'username': 'csrv2',
    'password': 'telnet',
}

csrv3 = {     
    'device_type': 'cisco_ios',
    'ip': '192.168.2.13',
    'username': 'csrv3',
    'password': 'telnet',
}

all_device = [csrv, csrv2, csrv3]    
    
for a_device in all_device:
        net_connect = ConnectHandler(**csrv)
        net_connect.enable()
        output = net_connect.send_command("show ip int brief")
        print output
