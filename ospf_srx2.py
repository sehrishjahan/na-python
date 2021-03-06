from datetime import datetime

from netmiko import ConnectHandler
from mydevices import srx2
import getpass

print "\n\n * * * * * * * * * *    CONFIGURING OSPF ON JUNIPER DEVICES    * * * * * * * * *  \n"

def check_ospf(net_connect, cmd='show route protocol ospf'):
    """Check whether oospf is currently configured on device. Return boolean"""
    output = net_connect.send_command_expect(cmd)
    return 'ospf' in output

def remove_ospf_config(net_connect, cmd='delete set protocol ospf area 0.0.0.0 interface ge-0/0/1.0', as_number=''):
    """Remove OSPF from the config"""
    ospf_cmd = "{} {}".format(cmd, str(as_number))
    cmd_list = [ospf_cmd]
    output = net_connect.send_config_set(cmd_list)
   # if net_connect.device_type == 'cisco_xr_ssh':
    #    output += net_connect.commit()
    print output

def configure_ospf(net_connect, file_name=''):
    """Configure OSPF on device."""
    try:
        output = net_connect.send_config_from_file(config_file=file_name)
        #if net_connect.device_type == 'cisco_xr_ssh':
         #   output += net_connect.commit()
        return output
    except IOError:
        print "Error reading file: {}".format(file_name)

def main():
    device_list = [srx2]
    print

    for a_device in device_list:
       # as_number = a_device.pop('as_number')
        as_number = 100
        net_connect = ConnectHandler(**a_device)
        
        net_connect.enable()
        #print "{}: {}".format(net_connect.device_type, net_connect.find_prompt())
        if check_ospf(net_connect):
            print "  OSPF is currently configured !!!!!\n"
            remove_ospf_config(net_connect, as_number=as_number)
        else:
            print "\n  No OSPF configured !!\n"

        # Check OSPF is now gone
        if check_ospf(net_connect):
            raise ValueError("OSPF configuration still detected")

        # Construct file_name based on device_type
        #device_type = net_connect.device_type
        #file_name = 'ospf_' + device_type.split("_ssh")[0] + '.txt'

        # Configure OSPF
        ospfconfig1 = configure_ospf(net_connect, 'ospf_srx2.txt')
        print ospfconfig1             
if __name__ == "__main__":
    main()
    
print "\n\n * * * * * * * * *   CONFIGURATION WAS DONE SUCCESSFULLY    * * * * * * * * * *  \n"
