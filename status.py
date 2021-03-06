from netmiko import ConnectHandler #imported netmiko library

 #initialized variables.
platform = 'cisco_ios'
host = '192.168.2.11'
username = 'cisco'

 #calling ConnectHandler function and passing in variables
net_connect = ConnectHandler(device_type=platform, ip=host, username='cisco', password='cisco1234')
net_connect.find_prompt()
 #using send_command() method to send the 'show ip int brief' command to router
print('\n                             MONITORING OF THE NETWORK                          \n')
print('\n                            INTERFACE STATUS ON CSRv1                           ')
print(' --------------------------------------------------------------------------------\n')
output = net_connect.send_command("show ip int brief")
print output
print('\n                             ROUTING TABLE                               ')
print(' --------------------------------------------------------------------------------\n')
output = net_connect.send_command("show ip route")
print output
print('\n                             BGP ROUTE TABLE                               ')
print(' --------------------------------------------------------------------------------\n')
output = net_connect.send_command("show ip bgp")
print output

#CSRV2
platform = 'cisco_ios'
host = '192.168.2.12'
username = 'cisco'
 #calling ConnectHandler function and passing in variables
net_connect = ConnectHandler(device_type=platform, ip=host, username='cisco', password='cisco1234')
net_connect.find_prompt()
 #using send_command() method to send the 'show ip int brief' command to router
print('\n                          INTERFACE STATUS ON CSRv2                             ')
print(' --------------------------------------------------------------------------------\n')
output = net_connect.send_command("show ip int brief")
print output
print('\n                             ROUTING TABLE                               ')
print(' --------------------------------------------------------------------------------\n')
output = net_connect.send_command("show ip route")
print output
print('\n                             BGP ROUTE TABLE                               ')
print(' --------------------------------------------------------------------------------\n')
output = net_connect.send_command("show ip bgp")
print output

#CSRV1
platform = 'cisco_ios'
host = '192.168.2.13'
username = 'cisco'
 #calling ConnectHandler function and passing in variables
net_connect = ConnectHandler(device_type=platform, ip=host, username='cisco', password='cisco1234')
net_connect.find_prompt() 
 #using send_command() method to send the 'show ip int brief' command to router
print('\n                             INTERFACE STATUS ON CSRv3                          ')
print(' --------------------------------------------------------------------------------\n')
output = net_connect.send_command("show ip int brief")
print output
print('\n                              ROUTING TABLE                               ')
print(' --------------------------------------------------------------------------------\n')
output = net_connect.send_command("show ip route")
print output
print('\n                              BGP ROUTE TABLE                               ')
print(' --------------------------------------------------------------------------------\n')
output = net_connect.send_command("show ip bgp")
print output

#SRX1
platform = 'juniper'
host = '192.168.2.14'
username = 'juniper'
password = 'cisco1234'
#calling ConnectHandler function and passing in variables
net_connect = ConnectHandler(device_type=platform, ip=host, username='juniper', password='cisco1234')
net_connect.find_prompt()
#using send_command() method to send the 'show configuration' command to router
print('\n                         INTERFACE STATUS ON SRX1                                  ')
print(' ----------------------------------------------------------------------------------\n')
output = net_connect.send_command("show interfaces terse")
print output
print('                             ROUTING TABLE                     ')
print(' -----------------------------------------------------------------------------------')
output = net_connect.send_command("show route ")
print output
    #SRX2
platform = 'juniper'
host = '192.168.2.15'
username = 'juniper'
password = 'cisco1234'
#calling ConnectHandler function and passing in variables
net_connect = ConnectHandler(device_type=platform, ip=host, username='juniper', password='cisco1234')
net_connect.find_prompt()
print('\n                          INTERFACE STATUS ON SRX2                                  ')
print(' ---------------------------------------------------------------------------------\n')
output = net_connect.send_command("show interfaces terse")
print output
print('                            ROUTING TABLE')
print(' ---------------------------------------------------------------------------------')
output = net_connect.send_command("show route")
print output
