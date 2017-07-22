from netmiko import ConnectHandler #imported netmiko library

#initialized variables.
platform = 'juniper'
host = '192.168.2.15'
username = 'juniper'
password = 'cisco1234'

#calling ConnectHandler function and passing in variables
net_connect = ConnectHandler(device_type=platform, ip=host, username='juniper', password='cisco1234')
net_connect.find_prompt()

#using send_command() method to send the 'show configuration' command to router
print('\n###############################################################################\n\n')
print('...................JUNIPER COMMAND SHOW CONFIGURATION OUTPUT....................\n\n')
output = net_connect.send_config_from_file(config_file=csrv2.py)
print output


