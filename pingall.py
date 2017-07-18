from netmiko import ConnectHandler #imported netmiko library
from devices import csrv, csrv2, csrv3
 def main ():
 device_list = [csrv, csrv2, csrv3]
 print 
 for a_device in device_list:
 net_connect = ConnectHandler(**a_device)
 print "{}: {}.format(net_connect.device_type, net_connect.find_prompt())
 
 if __name__ == "__main__":
 main()
