from netmiko import ConnectHandler

platform = 'cisco_ios'
host = '192.168.2.110'
username = 'csrv'
password = 'cisco1234'

#net_connect = ConnectHandler(**cisco_881)
net_connect = ConnectHandler(device_type=platform, ip=host, username='csrv', password='cisco1234')
net_connect.find_prompt()

