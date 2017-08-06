from netmiko import ConnectHandler #imported netmiko library
from mydevices import csrv1
#initialized variables.

#calling ConnectHandler function and passing in variables
net_connect = ConnectHandler(device_type=device_type, ip=ip, username='username', password='password')
net_connect.find_prompt()

#using send_command() method to send the 'show ip int brief' command to router
output = net_connect.send_command("show ip int brief")
print output

