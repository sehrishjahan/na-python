from netmiko import ConnectHandler
platform = 'cisco_ios'
host = '192.168.2.110'
username = 'csrv'
password = 'cisco1234'
device = ConnectHandler(device_type=platform, ip=host, username=username, password=password)
