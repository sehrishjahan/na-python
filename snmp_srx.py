from netmiko import ConnectHandler
from mydevices import srx1, srx2
import getpass

#from devices import srx1, srx2

def configure_snmp(net_connect, file_name=''):
    """Configure SNMP on device."""
    try:
        output = net_connect.send_config_from_file(config_file=file_name)
        return output
    except IOError:
        print "Error reading file: {}".format(file_name)

def main():
    device_list = [csrv1, csrv2, csrv3]
    print "\n              CONFIGURING SNMP PROTOCOL   "
    print 
  
    for a_device in device_list:
        net_connect = ConnectHandler(**a_device)
        
        net_connect.enable()
        #print "{}: {}".format(net_connect.device_type, net_connect.find_prompt()
       
         
        device_type = net_connect.device_type
        file_name = "snmp_" + (a_device ['username']) + ".txt"
        print "\n  Reading file : "
        print "  {}\n".format(file_name)
    
    # Configure SNMP
        snmpconfig = configure_snmp(net_connect, file_name)
        print snmpconfig
        print

if __name__ == "__main__":
  main()
