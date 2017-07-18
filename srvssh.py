 from netmiko import ConnectHandler
 net_connect=ConnectHandler(device_type='juniper',ip='192.168.2.101',username='juniper',password='juniper123')
 output=net_connect.send_command("show interface terse")
 print output
