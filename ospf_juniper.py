from datetime import datetime
from netmiko import ConnectHandler
from mydevices import srx1, srx2
import getpass
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
        return output
    except IOError:
        print "Error reading file: {}".format(file_name)

def main():
    device_list = [srx1, srx2]
    print "\n\n * * * * * * * * * *    CONFIGURING OSPF ON JUNIPER DEVICES    * * * * * * * * * *"                   
    print
    start_time = datetime.now()
    print
    
    for a_device in device_list:
        as_number = 100
        net_connect = ConnectHandler(**a_device)
        net_connect.enable()
        if check_ospf(net_connect):
            print "  OSPF is currently configured !!!!!\n"
            remove_ospf_config(net_connect, as_number=as_number)
        else:
            print "\n  No OSPF configured !!\n"

        # Check OSPF is now gone
        if check_ospf(net_connect):
            raise ValueError("OSPF configuration still detected")

        device_type = net_connect.device_type
        file_name = "ospf_" + str(a_device ['ip']) + ".txt"
        print "\n  Reading file : "
        print "  {}\n".format(file_name)
    
    # Configure OSPF
        bgpconfig = configure_ospf(net_connect, file_name)
        print bgpconfig
        print
   
    print "Time elapsed: {}\n".format(datetime.now() - start_time)

if __name__ == "__main__":
    main()
    
print "\n\n * * * * * * * * *   CONFIGURATION WAS DONE SUCCESSFULLY    * * * * * * * * * *  \n"
