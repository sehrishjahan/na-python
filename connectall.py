from datetime import datetime

from netmiko import ConnectHandler
from mydevices import srx1, srx2
import getpass

#from devices import srx1, srx2

def check_ospf(net_connect, cmd='show run protocol ospf'):
    """Check whether OSPF is currently configured on device. Return boolean"""
    output = net_connect.send_command_expect(cmd)
    return 'ospf' in output

def remove_ospf_config(net_connect, cmd='delete set ', process_id=''):
    """Remove OSPF from the config"""
    ospf_cmd = "{} {}".format(cmd, str(process_id))
    cmd_list = [ospf_cmd]
    output = net_connect.send_config_set(cmd_list)
   # if net_connect.device_type == 'cisco_ios':
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
    device_list = [srx1, srx2]
    print "\n              CONFIGURING OSPF PROTOCOL   "
    print 
    start_time = datetime.now()
    print
#     file_list = ['ospf_csrv1.txt', 'ospf_csrv2.txt', 'ospf_csrv3.txt'] 
    

    for a_device in device_list:
       # as_number = a_device.pop('process_id')
        print a_device
        process_id = 100
        net_connect = ConnectHandler(**a_device)
        
        net_connect.enable()
        #print "{}: {}".format(net_connect.device_type, net_connect.find_prompt())
        if check_ospf(net_connect):
              print "\n         OSPF currently configured   \n"
              remove_ospf_config(net_connect, process_id=process_id)
        else:
              print "\n         No OSPF"
   
        # Construct file name 
       
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
#         bgpconfig2 = configure_bgp(net_connect, 'bgp_csrv2.txt')
#         print bgpconfig2
#         bgpconfig3 = configure_bgp(net_connect, 'bgp_csrv3.txt')
#         print bgpconfig3
        
    
    print "Time elapsed: {}\n".format(datetime.now() - start_time)

if __name__ == "__main__":
    main()
