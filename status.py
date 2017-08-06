from datetime import datetime
from netmiko import ConnectHandler
from mydevices import csrv1, csrv2, csrv3
import getpass
def check_bgp(net_connect, cmd='show ip int br'):
   
    output = net_connect.send_command_expect(cmd)
    

def run_config(net_connect, cmd='shoe run'):
    """Remove BGP from the config"""
 
    print output

def configure_bgp(net_connect, file_name=''):
    """Configure BGP on device."""
    try:
        output = net_connect.send_config_from_file(config_file=file_name)
        #if net_connect.device_type == 'cisco_xr_ssh':
         #   output += net_connect.commit()
        return output
    except IOError:
        print "Error reading file: {}".format(file_name)

def main():
    device_list = [csrv1, csrv2, csrv3]
    print "\n              CONFIGURING BGP PROTOCOL   "
    print 
    start_time = datetime.now()
    print
    for a_device in device_list:
       # as_number = a_device.pop('as_number')
        print a_device
        print "\n STATUS ON CISCO " 
        net_connect = ConnectHandler(**a_device)
        
        net_connect.enable()
        if check_bgp(net_connect):
            print "\n         STATUS    \n"
            remove_bgp_config(net_connect, as_number=as_number)
        else:
            print "\n         No BGP"
        # Construct file name 
       
        # Check BGP is now gone
       
        
    print "Time elapsed: {}\n".format(datetime.now() - start_time)

if __name__ == "__main__":
    main()
    
print "\n\n * * * * * * * * *   CONFIGURATION WAS DONE SUCCESSFULLY    * * * * * * * * * *  \n"


