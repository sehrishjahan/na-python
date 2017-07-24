from datetime import datetime

from mydevices impport csrv2
from netmiko import ConnectHandler
import getpass

#from devices import csrv2

def check_ospf(net_connect, cmd='show run | inc router ospf'):
    """Check whether OSPF is currently configured on device. Return boolean"""
    output = net_connect.send_command_expect(cmd)
    return 'ospf' in output

def remove_ospf_config(net_connect, cmd='no router ospf', as_number=''):
    """Remove OSPF from the config"""
    ospf_cmd = "{} {}".format(cmd, str(as_number))
    cmd_list = [ospf_cmd]
    output = net_connect.send_config_set(cmd_list)
   # if net_connect.device_type == 'juniper':
    #    output += net_connect.commit()
    print output

def configure_ospf(net_connect, file_name=''):
    """Configure OSPF on device."""
    try:
        output = net_connect.send_config_from_file(config_file=file_name)
        #if net_connect.device_type == 'juniper':
         #   output += net_connect.commit()
        return output
    except IOError:
        print "Error reading file: {}".format(file_name)

def main():
    device_list = [csrv2, csrv3]
    print

    for a_device in device_list:
       # as_number = a_device.pop('as_number')
        as_number = 100
        net_connect = ConnectHandler(**a_device)
        
        net_connect.enable()
        #print "{}: {}".format(net_connect.device_type, net_connect.find_prompt())
        if check_ospf(net_connect):
            print "OSPF currently configured"
            remove_ospf_config(net_connect, as_number=as_number)
        else:
            print "No OSPF"

        # Check ospf is now gone
        if check_ospf(net_connect):
            raise ValueError("OSPF configuration still detected")

        # Construct file_name based on device_type
        #device_type = net_connect.device_type
        #file_name = 'ospf_' + device_type.split("_ssh")[0] + '.txt'

        # Configure OSPF
        bgpconfig1 = configure_ospf(net_connect, 'csrv2ospf.txt')
        bgpconfig2 = configure_ospf(net_connect, 'csrv3ospf.txt')
        print bgpconfig1
        print bgpconfig2

        
        

if __name__ == "__main__":
    main()
