from netmiko import ConnectHandler
from mydevices import csrv1

#initialized variables

#calling ConnectHandler function and passing in variables
net_connect = ConnectHandler(device_type=juniper, ip=ip, username=username, password=password)
net_connect.find_prompt()

#using send_command() method to send the 'show configuration' command to router
print('\n------------------------------------------------------------------------------\n')
print('...................JUNIPER COMMAND SHOW CONFIGURATION OUTPUT....................\n')
output = net_connect.send_command("show run ")
print output
print('\n-------------------------------------------------------------------------------\n')
print('...................JUNIPER COMMAND SHOW INTERFACES TERSE OUTPUT..................\n')
output = net_connect.send_command("show ip interfaces br ")
print output
