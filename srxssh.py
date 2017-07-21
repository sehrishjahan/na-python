from netmiko import ConnectHandler #imported netmiko library

#initialized variables.
platform = 'juniper'
host = '192.168.2.15'
username = 'juniper'
password = 'cisco1234'

#calling ConnectHandler function and passing in variables
net_connect = ConnectHandler(device_type=platform, ip=host, username='juniper', password='cisco1234')
net_connect.find_prompt()

#using send_command() method to send the 'show interfaces terse' command to router

output = net_connect.send_command("show ospf neighbor")
print output
