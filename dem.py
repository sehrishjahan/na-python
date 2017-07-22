from netmiko import ConnectHandler #imported netmiko library

#initialized variables.
platform = 'cisco_ios'
host = '192.168.2.12'
username = 'cisco'
password = 'cisco1234'

#calling ConnectHandler function and passing in variables
net_connect = ConnectHandler(device_type=platform, ip=host, username='cisco', password='cisco1234')
net_connect.find_prompt()

#using send_command() method to send the 'show configuration' command to router
print('\n###############################################################################\n\n')
print('................................csrv2 OSPF...................\n\n')
output = net_connect.send_config_from_file(config_file=csrv2.py)
print output


