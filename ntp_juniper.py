from netmiko import ConnectHandler
from mydevices import srx1,srx2
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
    print "\n              CONFIGURING NTP PROTOCOL   "
    print 
  
    for a_device in device_list:
        net_connect = ConnectHandler(**a_device)
        net_connect.enable()
        device_type = net_connect.device_type
        file_name = "ntp_" + (a_device ['username']) + ".txt"
        print "\n  Reading file : "
        print "  {}\n".format(file_name)
    # Configure NTP
        ntpconfig = configure_ntp(net_connect, file_name)
        print ntpconfig
        print
        print"\n    CLOCK TIMING"
        output = net_connect.send_command("show system uptime | match current")
        print output

if __name__ == "__main__":
  main()

print "\n\n  * * * * * * * * * * *    NTP SUCCESSFULLY CONFIGURED    * * * * * * * * * * *  \n"
