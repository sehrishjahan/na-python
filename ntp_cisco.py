from netmiko import ConnectHandler
from mydevices import csrv1, csrv2, csrv3
import getpass

#from devices import csrv, csrv2, csrv3

def configure_ntp(net_connect, file_name=''):
    """Configure NTP on device."""
    try:
        output = net_connect.send_config_from_file(config_file=file_name)
        return output
    except IOError:
        print "Error reading file: {}".format(file_name)

def main():
    device_list = [csrv1, csrv2, csrv3]
    print "\n              CONFIGURING NTP PROTOCOL   "
    print 
#     file_list = ['bgp_csrv1.txt', 'bgp_csrv2.txt', 'bgp_csrv3.txt'] 
  
    for a_device in device_list:
        net_connect = ConnectHandler(**a_device)
        
        net_connect.enable()
        #print "{}: {}".format(net_connect.device_type, net_connect.find_prompt()
       
         
        device_type = net_connect.device_type
        file_name = "ntp_" + (a_device ['username']) + ".txt"
        print "\n  Reading file : "
        print "  {}\n".format(file_name)
    
    # Configure NTP
        ntpconfig = configure_ntp(net_connect, file_name)
        print ntpconfig
        print
        print"\n    CLOCK TIMING"
        output = net_connect.send_command("show clock")
        print output

if __name__ == "__main__":
  main()

print "\n\n  * * * * * * * * * * *    NTP SUCCESSFULLY CONFIGURED    * * * * * * * * * * *  \n"
