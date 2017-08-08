from datetime import datetime
from netmiko import ConnectHandler
from mydevices import csrv1, csrv2, csrv3
import getpass
def check_bgp(net_connect, cmd='show run | inc router bgp'):
    """Check whether BGP is currently configured on device. Return boolean"""
    output = net_connect.send_command_expect(cmd)
    return 'bgp' in output

def remove_bgp_config(net_connect, cmd='no router bgp', as_number=''):
    """Remove BGP from the config"""
    bgp_cmd = "{} {}".format(cmd, str(as_number))
    cmd_list = [bgp_cmd]
    output = net_connect.send_config_set(cmd_list)
   # if net_connect.device_type == 'cisco_ios':
    #    output += net_connect.commit()
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
        as_number = 100
        net_connect = ConnectHandler(**a_device)
        
        net_connect.enable()
        if check_bgp(net_connect):
            print "\n         BGP currently configured   \n"
            remove_bgp_config(net_connect, as_number=as_number)
        else:
            print "\n         No BGP"
        # Construct file name 
       
        # Check BGP is now gone
        if check_bgp(net_connect):
            raise ValueError("BGP configuration still detected")
          
        device_type = net_connect.device_type
        file_name = "bgp_" + str(a_device ['ip']) + ".txt"
        print "\n  Reading file : "
        print "  {}\n".format(file_name)
    
    # Configure BGP
class MyError(Exception):
      def __init__(self, value):
             self.value = "% Invalid input detected at '^' marker."
      def __str__(self):
         return repr(self.value)

            try:
                raise MyError(2*2)
            except MyError as e:
            print 'My exception occurred, value:', e.value
        
        bgpconfig = configure_bgp(net_connect, file_name)
        print bgpconfig
        print
   
    print "Time elapsed: {}\n".format(datetime.now() - start_time)

if __name__ == "__main__":
    main()
    
print "\n\n * * * * * * * * *   CONFIGURATION WAS DONE SUCCESSFULLY    * * * * * * * * * *  \n"
