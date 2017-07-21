from netmiko import ConnectHandler
from datetime import datetime
csrv2 = {
'device_type':'cisco_ios',
'ip': '192.168.2.12',
'username': 'cisco',
'password':'cisco1234',
'verbose':False,
}
csrv3 = {
'device_type':'cisco_ios',
'ip': '192.168.2.13',
'username': 'cisco',
'password':'cisco1234',
'verbose':False,
}
juniper_srx = {
'device_type':'juniper',
'ip': '192.168.2.14',
'username': 'juniper',
'password':'cisco1234',
'verbose':False,
}
juniper_srx2 = {
'device_type':'juniper',
'ip': '192.168.2.15',
'username': 'juniper',
'password':'cisco1234',
'verbose':False,
}
all_devices =[csrv2, csrv3, juniper_srx, juniper_srx2]
start_time = datetime.now()
for a_device in all_devices:
     net_connect = ConnectHandler(**a_device)
     output = net_connect.send_command("show arp")
     print"\n\n^^^^^^ Device{0}^^^^^^^".format(a_device['device_type'])
     print output
     print">>>>>>>END>>>>>>>>>"
end_time = datetime.now()
total_time = end_time - start_time
