from netmiko import ConnectHandler #imported netmiko library

#initialized variables.
platform = 'juniper'
host = '192.168.2.101'
username = 'juniper'
password = 'juniper123'

#calling ConnectHandler function and passing in variables
net_connect = ConnectHandler(device_type=platform, ip=host, username='juniper', password='juniper123')
net_connect.find_prompt()

#using send_command() method to send the 'show ip int brief' command to router
output = net_connect.send_command("show interface terse")
print output
