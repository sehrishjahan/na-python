from netmiko import ConnectHandler #imported netmiko library

 #initialized variables.
platform = 'cisco_ios'
host = '192.168.2.11'
username = 'cisco'
 

 #calling ConnectHandler function and passing in variables

net_connect = ConnectHandler(device_type=platform, ip=host, username='cisco', password='cisco1234')
net_connect.find_prompt()
 
 #using send_command() method to send the 'show ip int brief' command to router
output = net_connect.send_command("show ip int brief")
print output

platform = 'cisco_ios'
host = '192.168.2.12'
username = 'cisco'
 

 #calling ConnectHandler function and passing in variables

net_connect = ConnectHandler(device_type=platform, ip=host, username='cisco', password='cisco1234')
net_connect.find_prompt()
 
 #using send_command() method to send the 'show ip int brief' command to router
output = net_connect.send_command("show ip int brief")
print output

platform = 'cisco_ios'
host = '192.168.2.13'
username = 'cisco'
 

 #calling ConnectHandler function and passing in variables

net_connect = ConnectHandler(device_type=platform, ip=host, username='cisco', password='cisco1234')
net_connect.find_prompt()
 
 #using send_command() method to send the 'show ip int brief' command to router
output = net_connect.send_command("show ip int brief")
print output

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
output = net_connect.send_command("show configuration ")
print output
print('\n################################################################################\n\n')
print('...................JUNIPER COMMAND SHOW INTERFACES TERSE OUTPUT................\n\n')
output = net_connect.send_command("show interfaces terse ")
print output
