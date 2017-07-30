from datetime import datetime

from netmiko import ConnectHandler
from mydevices import srx1, srx2
import getpass

def configure_ntp(net_connect, file_name=''):
    """Configure NTP on device."""
    try:
        output = net_connect.send_config_from_file(config_file=file_name)
        return output
    except IOError:
        print "Error reading file: {}".format(file_name)

def main():
    device_list = [srx1, srx2]
    print

    for a_device in device_list:
       
        net_connect = ConnectHandler(**a_device)
        
        net_connect.enable()
        #print "{}: {}".format(net_connect.device_type, net_connect.find_prompt())
       
        if check_ntp(net_connec
        # Construct file_name based on device_type
        #device_type = net_connect.device_type
        #file_name = 'ospf_' + device_type.split("_ssh")[0] + '.txt'

        # Configure OSPF
        ospfconfig1 = configure_ospf(net_connect, 'ospf_srx1.txt')
        print ospfconfig1             
if __name__ == "__main__":
    main()
    
print "\n\n * * * * * * * * *   CONFIGURATION WAS DONE SUCCESSFULLY    * * * * * * * * * *  \n"
