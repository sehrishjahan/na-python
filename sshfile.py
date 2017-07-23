from netmiko import ConnectHandler #imported netmiko library

#initialized variables.
platform = 'cisco_ios'
host = '192.168.2.11'
username = 'csrv'

#calling ConnectHandler function and passing in variables
net_connect = ConnectHandler(device_type=platform, ip=host, username='csrv', password='telnet')
net_connect.find_prompt()

#using send_command() method to send the 'show ip int brief' command to router
output = net_connect.send_command("show ip int brief")
print output

